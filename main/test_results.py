import json
import pytest as pytest
from main_task import get_mean_score, get_employment_status_count, get_score_ranges, get_enriched_bank_data
import pdb
@pytest.fixture
def reports(tmp_path):

    return "tests/reports/37599071.json"
    source_file = {
        "asd": 2,
        "hello": 5
    }

    with open(tmp_path / "report1.json", "w") as f:
        json.dump(source_file, f)

    source_file2 = {
        "asd3": 10,
        "hello": 8
    }

    with open(tmp_path / "report2.json", "w") as f:
        json.dump(source_file2, f)


    return [tmp_path / "report1.json", tmp_path / "report2.json"]

@pytest.fixture
def accounts(tmp_path):




    return {

    }

def test_mean(reports):
    total = 0

    x = open(reports)
    data = json.load(x)
    pdb.set_trace()


    assert total == 131