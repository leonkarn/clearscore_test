import json
import datetime

def latest_scores_with_date(reports):
    """
    takes as an input a list of paths to report json files and returns a dictionary with the account_id
    ,the latest credit score and the date
    :param reports:
    :return:
    """
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


def get_extracted_scores(reports):
    """
    reads a list of paths for reports and return only the latest credit scores as a list
    :param reports:
    :return:
    """
    user_credit = latest_scores_with_date(reports)
    credit_scores_list = []
    for user in user_credit:
        credit_scores_list.append(user_credit[user][1])
    return credit_scores_list


def create_range(scores):
    """
    takes a list of scores and return a dictionary with the range with step 50
    :param scores:
    :return:
    """
    out_range = {}
    for i in range(0, max(scores), 50):
        out_range[str(i) + "-" + str(i + 50)] = 0

    return out_range