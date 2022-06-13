import glob
import os
import json
import numpy as np
import datetime


print ("hello world")

reports_path = r"/Users/leonkarn/PycharmProjects/clearscore/bulk-reports/reports"
accounts_path = r"/Users/leonkarn/PycharmProjects/clearscore/bulk-reports/accounts"

reports = glob.glob(reports_path + r'/**/*.json', recursive=True)
accounts = glob.glob(accounts_path + r'/*.json', recursive=True)


# 1) Average credit score
credit_score_av = 0
credit_scores = []
for f in reports:
    x = open(f)
    data = json.load(x)
    credit_scores.append(int(data["report"]["ScoreBlock"]["Delphi"][0]["Score"]))

credit_score_av = np.mean(credit_scores)
print ("average credict score is", credit_score_av)

# 2)  number of users grouped by their employment status
employment_statutes = {}
for f in accounts:
    x = open(f)
    data = json.load(x)
    x = data["account"]["user"].get("employmentStatus")
    if x in employment_statutes:
        employment_statutes[x] += 1
    else:
        employment_statutes[x] = 1

print (employment_statutes)

# 3)  number of users in score ranges
print ("the max credit score is: ", max(credit_scores))
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

latest_credits = []

for user in user_credit:
    latest_credits.append(user_credit[user][1])

print ("these are the latest credits", latest_credits)
maximum_credit = max(latest_credits)
ranges = {}
for i in range(0, maximum_credit,50):
    ranges[str(i)+"-"+str(i+50)] = 0


for credit_score in latest_credits:

    for item in ranges:
        low_range = int(item.split("-")[0])
        high_range = int(item.split("-")[1])
        if credit_score>=low_range and credit_score< high_range:
            ranges[item] += 1
            break
print (ranges)

