"""
test_script.py
==========================
To test scrape_housing_data/script.py file
"""
import requests
import pytest
import json

@pytest.mark.vcr(allow_playback_repeats=True)
def test_scrape_data_from_mudah() -> None:
  
  # integration testing with pytest-recording: https://til.simonwillison.net/pytest/pytest-recording-vcr
  response = requests.get("https://search.mudah.my/v1/search",
                        params={"category": 2000,
                                "from": 0,
                                "limit": 200})
  json_output = response.json()
  # Check if the response (in dict) contains the "data" key
  assert "data" in json_output


@pytest.fixture(scope="session")
def json_dict(tmp_path_factory, mocker):
  path_to_data = tmp_path_factory.mktemp("output") / "data" / "2024-03-14.json"
  
  
  open(path_to_data, 'r') as file:
  data = json.load(file)
  print("File path exists")

  return data

def test_save_data_to_json(json_dict):
  assert json_dict == []

"""
def test_save_data_to_json_no_existing_file(mocker):
  # Use valid JSON for the initial file contents.
  mock_file_read_data = '[]'  # Represents an empty list in JSON.

  mocker.patch('scrape_housing_data.script.os.path.exists', return_value=True)
  mock_open = mocker.patch('scrape_housing_data.script.open', mocker.mock_open(read_data=mock_file_read_data))
  mock_json_dump = mocker.patch('scrape_housing_data.script.json.dump')

  # Simulate JSON response to be saved    
  response_mock = mocker.Mock()
  response_mock.json.return_value = {"data": "sample"}

  save_data_to_json(response_mock)

  mock_open.assert_called_once()
  mock_json_dump.assert_called_once()
"""