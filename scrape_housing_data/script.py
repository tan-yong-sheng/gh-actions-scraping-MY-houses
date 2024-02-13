"""
script.py
====================================
The core module of my example project
"""

import pathlib
import json
import datetime
import pytz
import requests
import warnings
import typing

warnings.filterwarnings("ignore")

def scrape_data_from_mudah(url: str ="https://search.mudah.my/v1/search",
                           headers: dict ={},
                           params: dict ={"category": 2000,
                                    "from": 0,
                                    "limit": 200}) -> dict:
    """Scrape mudah.my website for property listings, either for sale or rent.

    :return: A JSON response received from web requests 
    :rtype: dict
    """
    response = requests.get(url=url,
                            headers=headers,
                            params=params
                            )
    
    return response.json()["data"]


def open_json_file(filename: str) -> dict:
    """_summary_

    :param filename: _description_
    :type filename: str
    :raises ValueError: _description_
    :return: _description_
    :rtype: json
    """
    try:
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except ValueError:
                raise ValueError('{} is not valid JSON.'.format(filename))
    except FileNotFoundError:
        # if the file doesn't exists
        return {}

def append_data_to_json_file(data:list =[], filename: typing.Optional[str]=None) -> None:
    """Initialize an empty list or load existing data from the file

    :param data: _description_, defaults to []
    :type data: list, optional
    :param filename: _description_, defaults to None
    :type filename: typing.Optional[str], optional
    """
    if filename is None:
        data_folder = 'output/data'
        now = datetime.datetime.now(tz=pytz.timezone("Asia/Kuala_Lumpur"))
        p = pathlib.Path(__file__).parent.parent
        filename = p.joinpath(data_folder, f"{now:%Y-%m-%d}.json")

    # Extend the existing data with the new JSON output
    json_data = open_json_file(filename)
    data.extend(json_data)

    # Save the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


def main():
    """
    Execute the workflows of this project. It performs the following:

    1. Use `scrape_data` function to scrape data for property listings.
    2. Save the scraped JSON data into a list.
    3. Persist the data by writing it to a JSON file.
    """
    
    mudah_housing_data = scrape_data_from_mudah()
    append_data_to_json_file(data=mudah_housing_data)


if __name__ == "__main__":
    main()