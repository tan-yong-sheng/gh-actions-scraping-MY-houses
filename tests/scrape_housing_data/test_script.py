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
  # integration testing with pytest-vcr: https://medium.com/pythonistas/integration-testing-like-a-boss-with-pytest-vcr-72352c8c65fd
  response = requests.get("https://search.mudah.my/v1/search",
                        params={"category": 2000,
                                "from": 0,
                                "limit": 200})
  # Check if the response (in dict) contains the "data" key
  assert "data" in response.json()
  

  
