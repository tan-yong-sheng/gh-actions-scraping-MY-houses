"""
test_script.py
==========================
To test scrape_housing_data/script.py file
"""
import requests
import pytest
from scrape_housing_data.script import scrape_data_from_mudah

@pytest.mark.vcr(allow_playback_repeats=True)
def test_scrape_data_from_mudah() -> None:
  # integration testing with pytest-recording: https://til.simonwillison.net/pytest/pytest-recording-vcr
  response = requests.get("https://search.mudah.my/v1/search",
                        params={"category": 2000,
                                "from": 0,
                                "limit": 200})
  # Check if the response (in dict) contains the "data" key
  assert "data" in response.json()



"""
Error to solve
Traceback (most recent call last):
  File "/home/runner/work/gh-actions-scraping-MY-houses/gh-actions-scraping-MY-houses/scrape_housing_data/script.py", line 75, in <module>
    main()
  File "/home/runner/work/gh-actions-scraping-MY-houses/gh-actions-scraping-MY-houses/scrape_housing_data/script.py", line 68, in main
    save_data_to_json(mudah_housing_data)
  File "/home/runner/work/gh-actions-scraping-MY-houses/gh-actions-scraping-MY-houses/scrape_housing_data/script.py", line 56, in save_data_to_json
    data.extend(json_output)
UnboundLocalError: local variable 'data' referenced before assignment

"""

  
