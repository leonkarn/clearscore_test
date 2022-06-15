import json
import datetime

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


def create_range(scores):

    out_range = {}
    for i in range(0, max(scores), 50):
        out_range[str(i) + "-" + str(i + 50)] = 0

    return out_range