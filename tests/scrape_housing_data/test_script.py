"""
test_script.py
==========================
To test scrape_housing_data/script.py file
"""
import requests
import pytest
from scrape_housing_data.script import scrape_data_from_mudah

@pytest.mark.vcr
def test_scrape_data_from_mudah() -> None:
  response = requests.get("https://search.mudah.my/v1/search",
                        params={"category": 2000,
                                "from": 0,
                                "limit": 200})
  assert "data" in response.json()
