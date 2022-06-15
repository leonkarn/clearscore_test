import json
import pytest as pytest
from main_task import get_mean_score, get_employment_status_count, get_score_ranges, get_enriched_bank_data

@pytest.fixture
def reports(tmp_path):
    report1 = {
        "account-id": "351300",
        "client-ref": "0021999178-1515157993",
        "bureau-id": "EX",
        "pulled-timestamp": "2018-01-05T13:13:13",
        "report-id": "38157329",
        "report": {
                    "ScoreBlock": {
                        "Delphi": [
                            {
                                "ScoreName": "Delphi New Business G4.1 Banki ",
                                "Scorecard_Identifier": "402",
                                "RequestID": "17",
                                "Score": "535",
                                "ReasonCode": "D205D209D201D202D204"
                            }
                        ]
                    },
                    "Summary": {
                        "Payment_Profiles": {
                            "CPA": {
                                "Bank": {
                                    "Total_number_of__active_non_delinquent_CPA_accounts_opened_L6m": "0",
                                    "Total_number_of_Bank_Active_accounts_": "0",
                                    "Total_value_of_Bank_Delinquent_accounts": "6323",
                                    "Percent_0_Arrears_of_Last_12_Bank_Available_Histories": "0",
                                    "Total_Credit_Limit_of_Fixed_Installment_Bank_PPS": "0",
                                    "Total_outstanding_balance_on_Bank_active_accounts": "0",
                                    "Total_Balance_of_Fixed_Installment_Bank_PPs": "0",
                                    "Total_Installment_of_Bank_Open_Account_PPs": "0",
                                    "Number_of_Bank_Fixed_Installment_PPs_Ever": "0",
                                    "Worst_current_status_on_active_non_delinquent_non_revolving_accounts": "",
                                    "Number_of_Habitually_Slow_Bank_PPs": "0",
                                    "Outstanding_Balance_on_delinquent_revolving_CPA_accounts": "0",
                                    "Percent_0_Arrears_of_Last_24_Bank_Available_Histories": "0",
                                    "Number_of_Times_3_Arrears_of_Last_6_Bank_Available_Histories": "6",
                                    "Percent_2_Arrears_of_Last_12_Bank_Available_Histories": "100",
                                    "Number_of_Bank_PPs_Ever": "1",
                                    "Number_of_Times_0_Arrears_of_Last_3_Bank_Available_Histories": "0",
                                    "Number_of_Bank_accounts_opened_4to12_months_ago": "0",
                                    "Number_of_Times_1_Arrears_of_Last_12_Bank_Available_Histories": "12",
                                    "Number_of_Times_2_Arrears_of_Last_6_Bank_Available_Histories": "6",
                                    "Total_Balance_of_Bank_Open_Account_PPs": "0",
                                    "Number_of_Closed_Revolving_Bank_PPs": "0",
                                    "Days_since_most_recent_Bank_Delinquent_CPA__account_": "79",
                                    "Percent_0_Arrears_of_Last_3_Bank_Available_Histories": "0",
                                    "Number_of_Times_1_Arrears_of_Last_6_Bank_Available_Histories": "6",
                                    "Percent_3_Arrears_of_Last_6_Bank_Available_Histories": "100",
                                    "Worst_Arrears_on_Any_Bank_PPs": "W",
                                    "Capital_Amount_of_Bank_PPs_Opened_in_the_Last_2_Years": "4000",
                                    "Number_of_Bank_PPs_in_the_Last_5_Years": "1",
                                    "Worst_status_in_the_last_3_months_for_active_non_delinquent_CPA_accounts_opened_in_the_last_12_months": "",
                                    "Number_of_Times_0_Arrears_of_Last_12_Bank_Available_Histories": "0",
                                    "Number_of_Disputed_Bank_PPs": "0"
                                }
                            }
                        },
                        "user-uuid": "1bc25bc6-9a63-4ea7-ab83-fb764399da7b"
                    }


        }
    }
    report2 = {
   "account-id": "337200",
   "client-ref": "0067555056-1515869677",
   "bureau-id": "EX",
   "pulled-timestamp": "2018-01-13T18:54:37",
   "report-id": "38261311",
   "report": {
      "ScoreBlock": {
         "Delphi": [
            {
               "ScoreName": "Delphi New Business G4.1 Banki ",
               "Scorecard_Identifier": "403",
               "RequestID": "17",
               "Score": "614",
               "ReasonCode": "D305D310D306D301D302"
            }
         ]
      },
      "Summary": {
         "Payment_Profiles": {
            "CPA": {
               "Bank": {
                  "Total_number_of__active_non_delinquent_CPA_accounts_opened_L6m": "1",
                  "Capital_Amount_of_Bank_PPs_Opened_in_the_Last_Year": "5000",
                  "Number_of_Bank_accounts_opened_for_at_least_12_months": "0",
                  "Number_of_Times_2_Arrears_of_Last_3_Bank_Available_Histories": "0",
                  "Worst_Current_Status_on_active_Bank_CPA_accounts": "0",
                  "Number_of_Open_Fixed_Installment_Bank_PPs": "0",
                  "Percent_0_Arrears_of_Last_6_Bank_Available_Histories": "100",
                  "Worst_Arrears_Level_of_Most_Recent_Bank_Opened_PP": "0",
                  "Percent_3_Arrears_of_Last_24_Bank_Available_Histories": "0",
                  "Total_number_of_Bank_Delinquent_Accounts": "0",
                  "Number_of_Times_2_Arrears_of_Last_24_Bank_Available_Histories": "0",
                  "Worst_status_in_the_last_3_months_on_Bank_accounts_opened_4to12_months_ago": "0",
                  "Number_of_Times_1_Arrears_of_Last_24_Bank_Available_Histories": "0",
                  "Worst_status_in_the_last_4to6_months_for_Bank_active_non_delinquent_CPA_accounts_": "0",
                  "Percent_1_Arrears_of_Last_6_Bank_Available_Histories": "0",
                  "Number_of_Bank_PPs_in_the_Last_30_Days": "0",
                  "Current_Balance_of_Bank_PPs": "398",
                  "Number_of_Currently_Open_Bank_PPs": "1",
                  "Monthly_Installment_Value_of_Currently_Open_Bank_PPs": "398",
                  "Number_of_Bank_PPs_in_the_Last_180_Days": "1",
                  "Number_of_Bank_PPs_in_the_Last_3_Years": "1",
                  "Percent_3_Arrears_of_Last_12_Bank_Available_Histories": "0",
                  "Total_number_of_Bank_Active_accounts_": "1",
                  "Total_value_of_Bank_Delinquent_accounts": "0",
                  "Percent_0_Arrears_of_Last_12_Bank_Available_Histories": "100",
                  "Worst_Arrears_on_Open_Bank_PPs": "0",
                  "Number_of_Written_Off_Bank_PPs": "0",
                  "Capital_Amount_of_Bank_PPs_Opened_in_the_Last_30_Days": "0",
                  "Percent_2_Arrears_of_Last_3_Bank_Available_Histories": "0",
                  "Number_of_Times_0_Arrears_of_Last_24_Bank_Available_Histories": "4",
                  "Total_Credit_Limit_of_Fixed_Installment_Bank_PPS": "0",
                  "Number_of_Closed_Fixed_Installment_Bank_PPs": "0",
                  "Percent_3_Arrears_of_Last_3_Bank_Available_Histories": "0",
                  "Total_Credit_Limit_of_Revolving_Bank_PPs": "0",
                  "Number_of_Bank_Revolving_PPs_Ever": "0",
                  "Total_Balance_of_Revolving_Bank_PPs": "0",
                  "Total_Credit_Limit_of_Bank_Open_Account_PPs": "0",
                  "Percent_1_Arrears_of_Last_3_Bank_Available_Histories": "0",
                  "Total_outstanding_balance_on_Bank_active_accounts": "398",
                  "Months_Since_Most_Recent_Opened_Bank_PPs": "5",
                  "Worst_status_last_3_months_for_active__non_delinquent_CPA_accounts_opened_for_more_than_12months_": "",
                  "Percent_1_Arrears_of_Last_12_Bank_Available_Histories": "0",
                  "Number_of_Times_2_Arrears_of_Last_12_Bank_Available_Histories": "0",
                  "Months_Since_Oldest_Opened_Bank_PPs": "5",
                  "Number_of_Times_3_Arrears_of_Last_3_Bank_Available_Histories": "0",
                  "Number_of_Bank_PPs_in_the_Last_Year": "1",
                  "Number_of_Times_1_Arrears_of_Last_3_Bank_Available_Histories": "0",
                  "Percent_1_Arrears_of_Last_24_Bank_Available_Histories": "0",
                  "Worst_Arrears_on_Bank_PPs_in_the_Last_Year": "0",
                  "Percent_2_Arrears_of_Last_6_Bank_Available_Histories": "0",
                  "Total_Balance_of_Fixed_Installment_Bank_PPs": "0",
                  "Total_Installment_of_Bank_Open_Account_PPs": "0",
                  "Number_of_Bank_Fixed_Installment_PPs_Ever": "0",
                  "Worst_current_status_on_active_non_delinquent_non_revolving_accounts": "0",
                  "Number_of_Habitually_Slow_Bank_PPs": "0",
                  "Outstanding_Balance_on_delinquent_revolving_CPA_accounts": "0",
                  "Percent_0_Arrears_of_Last_24_Bank_Available_Histories": "100",
                  "Worst_status_in_the_last_6_months_on_Bank_accounts_opened_4to12_months_ago": "0",
                  "Worst_status_in_the_last_3_months_on_Bank_accounts_opened_for_at_least_12_months": "",
                  "Number_of_Closed_Bank_PPs": "0",
                  "Capital_Amount_of_Bank_PPs_Opened_in_the_Last_180_Days": "5000",
                  "Monthly_CPA_Installment_Bank": "0",
                  "Outstanding_CPA_Balance_Bank": "0",
                  "Capital_Amount_of_Bank_PPs_Opened_in_the_Last_90_Days": "0",
                  "Worst_Arrears_on_Closed_Bank_PPs": "",
                  "Number_of_Bank_PPs_in_the_Last_90_Days": "0",
                  "Worst_status_in_the_last_6_months_on_Bank_accounts_opened_for_at_least_12_months": "",
                  "Worst_current_status_on_active_non_delinquent_revolving_accounts": "",
                  "Number_of_Absconded_Bank_PPs": "0",
                  "Worst_Arrears_on_Bank_PPs_in_the_Last_90_Days": "0",
                  "Total_Installment_of_Revolving_Bank_PPs": "0",
                  "Number_of_Times_3_Arrears_of_Last_12_Bank_Available_Histories": "0",
                  "Total_Installment_of_Fixed_Installment_Bank_PPs": "0",
                  "Number_of_Times_0_Arrears_of_Last_6_Bank_Available_Histories": "4",
                  "Number_of_Open_Revolving_Bank_PPs": "0",
                  "Number_of_Bank_PPs_in_the_Last_4_Years": "1",
                  "Worst_Arrears_on_Bank_PPs_in_the_Last_180_Days": "0",
                  "Number_of_Times_3_Arrears_of_Last_24_Bank_Available_Histories": "0",
                  "Number_of_Bank_PPs_in_the_Last_2_Years": "1",
                  "Percent_2_Arrears_of_Last_24_Bank_Available_Histories": "0",
                  "Outstanding_Balance_on_non_delinquent_revolving_CPA_opened_L6m": "0",
                  "Number_of_Times_3_Arrears_of_Last_6_Bank_Available_Histories": "0",
                  "Percent_2_Arrears_of_Last_12_Bank_Available_Histories": "0",
                  "Number_of_Bank_PPs_Ever": "1",
                  "Number_of_Times_0_Arrears_of_Last_3_Bank_Available_Histories": "3",
                  "Number_of_Bank_accounts_opened_4to12_months_ago": "1",
                  "Number_of_Times_1_Arrears_of_Last_12_Bank_Available_Histories": "0",
                  "Number_of_Times_2_Arrears_of_Last_6_Bank_Available_Histories": "0",
                  "Total_Balance_of_Bank_Open_Account_PPs": "0",
                  "Number_of_Closed_Revolving_Bank_PPs": "0",
                  "Days_since_most_recent_Bank_Delinquent_CPA__account_": "",
                  "Percent_0_Arrears_of_Last_3_Bank_Available_Histories": "100",
                  "Number_of_Times_1_Arrears_of_Last_6_Bank_Available_Histories": "0",
                  "Percent_3_Arrears_of_Last_6_Bank_Available_Histories": "0",
                  "Worst_Arrears_on_Any_Bank_PPs": "0",
                  "Capital_Amount_of_Bank_PPs_Opened_in_the_Last_2_Years": "5000",
                  "Number_of_Bank_PPs_in_the_Last_5_Years": "1",
                  "Worst_status_in_the_last_3_months_for_active_non_delinquent_CPA_accounts_opened_in_the_last_12_months": "0",
                  "Number_of_Times_0_Arrears_of_Last_12_Bank_Available_Histories": "4",
                  "Number_of_Disputed_Bank_PPs": "0"
               }
            }
         },
         "user-uuid": "0f331b0b-f1a2-4e5d-8284-33ca9bf41254"
      }
   }
}

    with open(tmp_path / "report1.json", "w") as f:
        json.dump(report1, f)


    with open(tmp_path / "report2.json", "w") as f:
        json.dump(report2, f)


    return [tmp_path / "report1.json", tmp_path / "report2.json"]

@pytest.fixture
def accounts(tmp_path):
    account1 = {
        "uuid": "0f331b0b-f1a2-4e5d-8284-33ca9bf41254",
        "marketId": "ZA",
        "accountId": 337200,
        "account": {
            "user": {
                "bankName": "CAPITEC",
                "dateOfBirth": "1959-05",
                "employmentStatus": "FT_EMPLOYED",
                "salary": {
                    "amount": 20,
                    "type": "MONTHLY",
                    "currency": "ZAR"
                },
                "id": 337200,
                "idDocuments": [
                    {
                        "type": "NATIONALID",
                        "value": "xxx"
                    }
                ],
                "residentialStatus": "WITH_PARENTS"
            }
        },
        "schemaVersion": "CS-1"
    }
    account2 = {
       "uuid": "1bc25bc6-9a63-4ea7-ab83-fb764399da7b",
       "marketId": "ZA",
       "accountId": 351300,
       "account": {
          "user": {
             "bankName": "CAPITEC",
             "dateOfBirth": "1977-06",
             "employmentStatus": "FT_EMPLOYED",
             "salary": {
                "amount": 19000,
                "type": "MONTHLY",
                "currency": "ZAR"
             },
             "id": 351300,
             "idDocuments": [
                {
                   "type": "NATIONALID",
                   "value": "xxx"
                }
             ],
             "residentialStatus": "WITH_PARENTS"
          }
       },
       "schemaVersion": "CS-1"
    }

    with open(tmp_path / "account1.json", "w") as f:
        json.dump(account1, f)

    with open(tmp_path / "account2.json", "w") as f:
        json.dump(account2, f)

    return [tmp_path / "account1.json", tmp_path / "account2.json"]

def test_average_score(reports):
    # 535 + 614 / 2
    avg_score = get_mean_score(reports)
    assert avg_score["avg_credit_score"] == 574.5


def test_status(accounts):
    status_count = get_employment_status_count(accounts)
    employed = status_count["FT_EMPLOYED"]

    assert employed == 2

def test_credit_score_range(reports):
    x = get_score_ranges(reports)
    assert x["500-550"] == 1
    assert x["600-650"] == 1