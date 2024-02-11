"""
test_script.py
==========================
To test scrape_housing_data/script.py file
"""
import requests
from scrape_housing_data.script import scrape_data_from_mudah

def test_scrape_data_from_mudah(mocker):
  requests_mock = mocker.patch("scrape_housing_data.script.requests.get")
  requests_mock.return_value = requests.get("https://search.mudah.my/v1/search",
                            params={"category": 2000,
                                    "from": 0,
                                    "limit": 200})
  assert type(scrape_data_from_mudah()) == dict

  

