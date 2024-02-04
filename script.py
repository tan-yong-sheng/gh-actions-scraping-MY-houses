#!/usr/bin/env python3

import os
import pathlib
from stat import *
import datetime
import json
import requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import warnings

warnings.filterwarnings("ignore")

# for you to change easily
data_folder = 'data'
now = datetime.datetime.utcnow()
p = pathlib.Path(os.path.dirname(__file__))
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
def scrape_data():
    response = requests.get("https://search.mudah.my/v1/search",
                       params={"category":2000,
                               "from":0,
                               "limit":200},
                                        # Get Random User Agent String.
                        headers={"User-Agent": user_agent_rotator.get_random_user_agent()})

    json_output = response.json()["data"]
    data.extend(json_output)


# execute and persist data
async def main():
    scrape_data()
    # persist data
    with open(path_to_data, 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
