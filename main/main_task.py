import glob
import json
import numpy as np
import datetime
import pandas as pd
from utils import latest_scores_with_date, create_range, get_latest_scores
import os

reports_path = r"./bulk-reports/reports"
accounts_path = r"./bulk-reports/accounts"

reports = glob.glob(reports_path + r'/**/*.json', recursive=True)
accounts = glob.glob(accounts_path + r'/*.json', recursive=True)

# 1) Average credit score
def get_mean_score(reports):
    """
    get the list of report path as an input. reads all of them and return a dictionary with the average score
    :param reports: list of paths
    """
    credit_scores = []
    for f in reports:
        x = open(f)
        data = json.load(x)
        credit_scores.append(int(data["report"]["ScoreBlock"]["Delphi"][0]["Score"]))
    credit_score_av = np.mean(credit_scores)
    average_score = {"avg_credit_score": credit_score_av}
    return average_score

# 2)  number of users grouped by their employment status
def get_employment_status_count(accounts):
    """
    gets a list of account file paths and reads them. It counts the employments statutes and returns a dictionnary
    with the count per each status
    :param accounts: list of paths for accounts
    :return:
    """
    employment_statutes = {}
    for f in accounts:
        x = open(f)
        data = json.load(x)
        try:
            status = data["account"]["user"]["employmentStatus"]
        except KeyError:
            status = "UNKNOWN"
        if status in employment_statutes:
            employment_statutes[status] += 1
        else:
            employment_statutes[status] = 1

    return employment_statutes

# 3)  number of users in score ranges
def get_score_ranges(reports):
    """
    it takes the list of report paths as an input and reads them. It returns a dictionnary with the range of credit
    scores and how many people are in each range.
    :param reports: list of paths
    :return:
    """
    latest_scores = get_latest_scores(reports)
    ranges = create_range(latest_scores)

    for credit_score in latest_scores:
        for item in ranges:
            low_range = int(item.split("-")[0])
            high_range = int(item.split("-")[1])
            if credit_score >= low_range and credit_score < high_range:
                ranges[item] += 1
                break
    return ranges


# 4) enriched bank data
def get_enriched_bank_data(accounts, reports):
    """
    It reads both account and reports and returns a dictionaary with uuid, employment_status,bank_name,
    active_bank_accounts and balance
    :param accounts: list of paths
    :param reports: list of paths
    :return:
    """
    bank_data_enriched = {}
    user_credit = latest_scores_with_date(reports)
    for f in accounts:
        x = open(f)
        data = json.load(x)
        bank_data_enriched[data["accountId"]] = {"uuid": data["uuid"],
                                                 "employment_status": data["account"]["user"].get("employmentStatus"),
                                                 "bank_name": data["account"]["user"].get("bankName")}

    for f in reports:
        x = open(f)
        data = json.load(x)
        account_id = data["account-id"]
        date_pulled = data["pulled-timestamp"]
        date = datetime.datetime.strptime(date_pulled, "%Y-%m-%dT%H:%M:%S")
        if date == user_credit[account_id][0]:
            bank_data_enriched[int(account_id)]["active_bank_accounts"] = \
            data["report"]["Summary"]["Payment_Profiles"]["CPA"]["Bank"]["Total_number_of_Bank_Active_accounts_"]
            bank_data_enriched[int(account_id)]["balance"] = data["report"]["Summary"]["Payment_Profiles"]["CPA"]["Bank"][
                "Total_outstanding_balance_on_Bank_active_accounts"]

    return bank_data_enriched

if not os.path.exists("output"):
    os.mkdir("output")
# 1
df = pd.DataFrame.from_dict([get_mean_score(reports)])
df.to_csv("output/average_mean.csv", index=False, header=True)

# 2
df = pd.DataFrame.from_dict([get_employment_status_count(accounts)])
df.to_csv("output/employment_statutes_count.csv", index=True, header=True)

# 3
df = pd.DataFrame.from_dict([get_score_ranges(reports)])
df.to_csv("output/ranges_count.csv", index=False, header=True)

# 4
df = pd.DataFrame.from_dict(get_enriched_bank_data(accounts, reports), orient='index')
df.to_csv("output/bank_data_enriched.csv", index=True, header=True)