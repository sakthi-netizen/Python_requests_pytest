import pytest
import os
import json
import pytz
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata"))
    timestamp = ist_time.strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{timestamp}.html"

@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("\nSetting up the test environment")
    yield
    print("\nTearing down the test environment")
