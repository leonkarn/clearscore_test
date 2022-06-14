import glob
import os
import json
import numpy as np
import datetime

reports_path = r"./bulk-reports/reports"
accounts_path = r"./bulk-reports/accounts"

reports = glob.glob(reports_path + r'/**/*.json', recursive=True)
accounts = glob.glob(accounts_path + r'/*.json', recursive=True)

# 1) Average credit score
def get_mean_score(reports):
    # credit_score_av = 0
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
    employment_statutes = {}
    for f in accounts:
        x = open(f)
        data = json.load(x)
        x = data["account"]["user"].get("employmentStatus")
        if x in employment_statutes:
            employment_statutes[x] += 1
        else:
            employment_statutes[x] = 1

    return employment_statutes

def latest_scores_with_date(reports):
    user_credit = {}
    for f in reports:
        x = open(f)
        data = json.load(x)
        score = (int(data["report"]["ScoreBlock"]["Delphi"][0]["Score"]))
        account_id = data["account-id"]
        date_pulled = data["pulled-timestamp"]
        date = datetime.datetime.strptime(date_pulled, "%Y-%m-%dT%H:%M:%S")
        if account_id not in user_credit:
            user_credit[account_id] = (date, score)
        else:
            if date > user_credit[account_id][0]:
                user_credit[account_id] = (date, score)
    return user_credit


def get_latest_scores(reports):

    user_credit = latest_scores_with_date(reports)
    credit_scores_list = []
    for user in user_credit:
        credit_scores_list.append(user_credit[user][1])
    return credit_scores_list


def create_range(latest_scores):

    out_range = {}
    for i in range(0, max(latest_scores), 50):
        out_range[str(i) + "-" + str(i + 50)] = 0

    return out_range


# 3)  number of users in score ranges
def get_score_ranges(reports):
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

# 1
with open("output/average.json", "w") as outfile:
    json.dump(get_mean_score(reports), outfile)

# 2
with open("output/employment_statuses.json", "w") as outfile:
    json.dump(get_employment_status_count(accounts), outfile, indent=4)

# 3
with open("output/ranges_count.json", "w") as outfile:
    json.dump(get_score_ranges(reports), outfile, indent=4)

4
with open("output/bank_data_enriched.json", "w") as outfile:
    json.dump(get_enriched_bank_data(accounts, reports), outfile, indent=4)
