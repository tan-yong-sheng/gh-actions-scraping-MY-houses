"""
script.py
====================================
The core module of my example project
"""

import os
import pathlib
from stat import *
import datetime
import pytz
import json
import requests
import warnings

warnings.filterwarnings("ignore")

data_folder = 'output/data'
now = datetime.datetime.now(tz=pytz.timezone("Asia/Kuala_Lumpur"))
p = pathlib.Path(os.path.dirname(os.path.dirname(__file__)))
path_to_data = p.joinpath(data_folder, f"{now:%Y-%m-%d}.json")
data = []

"""
    
    The data wil be saved it into a list of JSON objects.

    :param response: 
    :type response: requests.Response
    """


def scrape_data_from_mudah():
    """Scrape mudah.my website for property listings, either for sale or rent.

    :return: A JSON response received from web requests 
    :rtype: dict
    """
    response = requests.get("https://search.mudah.my/v1/search",
                            params={"category": 2000,
                                    "from": 0,
                                    "limit": 200})
    json_output = response.json()["data"]
    return json_output


def save_data_to_json(json_output):
    """Save the web requests data in form of 

    :param json_output: _description_
    :type json_output: _type_
    """
    if os.path.exists(path_to_data):
        with open(path_to_data, 'r') as file:
            data = json.load(file)   
    data.extend(json_output)

# execute and persist data
def main():
    """
    Execute the workflows of this project. It performs the following:

    1. Use `scrape_data` function to scrape data for property listings.
    2. Save the scraped JSON data into a list.
    3. Persist the data by writing it to a JSON file.
    """
    mudah_housing_data = scrape_data_from_mudah()
    save_data_to_json(mudah_housing_data)
    
    # persist data
    with open(path_to_data, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    main()
