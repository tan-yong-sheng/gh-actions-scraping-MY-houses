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
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import warnings
import asyncio

warnings.filterwarnings("ignore")

# for you to change easily
data_folder = 'data'
now = datetime.datetime.now(tz=pytz.timezone("Asia/Kuala_Lumpur"))
p = pathlib.Path(os.path.dirname(os.path.dirname(__file__)))
path_to_data = p.joinpath(data_folder, f"{now:%Y-%m-%d}.json")
print(os.path.dirname(__file__))
print(path_to_data)

# read data, if needed
data = []
if os.path.exists(path_to_data):
    with open(path_to_data, 'r') as file:
        data = json.load(file)

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


# scrape housing data from mudah.my
def get_data_from_mudah():
    """
    Scrape mudah.my website for property listing, either sell or let
    """
    response = requests.get("https://search.mudah.my/v1/search",
                       params={"category":2000,
                               "from":0,
                               "limit":200},
                                        # Get Random User Agent String.
                        headers={"User-Agent": user_agent_rotator.get_random_user_agent()})
    return response


def scrape_data(response):
    """_summary_

    Parameters
    ----------
    response : 
    """
    json_output = response.json()["data"]
    data.extend(json_output)


# execute and persist data
async def main():
    """
    Asynchronous function to execute the workflows of this project. It executes the following:
    1. Using `scrape_data` function to scrape data for property listing
    2. Save the scraped json data into a list
    """
    mudah_housing_data = get_data_from_mudah()
    
    scrape_data(mudah_housing_data) 
    
    # persist data
    with open(path_to_data, 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    asyncio.run(main())