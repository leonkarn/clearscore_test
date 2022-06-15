import json
import pytest as pytest
from main_task import get_mean_score, get_employment_status_count, get_score_ranges, get_enriched_bank_data
import pdb
# @pytest.fixture
# def reports(tmp_path):
#
#     return "tests/reports/37599071.json"
#     source_file = {
#         "asd": 2,
#         "hello": 5
#     }
#
#     with open(tmp_path / "report1.json", "w") as f:
#         json.dump(source_file, f)
#
#     source_file2 = {
#         "asd3": 10,
#         "hello": 8
#     }
#
#     with open(tmp_path / "report2.json", "w") as f:
#         json.dump(source_file2, f)
#
#
#     return [tmp_path / "report1.json", tmp_path / "report2.json"]
#
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




def test_status(accounts):
    status_count = get_employment_status_count(accounts)
    employed = status_count["FT_EMPLOYED"]

    assert employed == 2