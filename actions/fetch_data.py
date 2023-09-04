import os

import requests

from misc import get_urls
from settings import SAVED_DATA_FOLDER


def fetch_data():
    urls = get_urls()

    if len(urls) == 0:
        print("There are no URLs!\n")
        return

    print("Fetching data...\n")

    for url in urls:
        print(f"\tFetching URL '{url['url']}'...")
        r = requests.get(url["url"])

        if r.status_code != 200:
            print(f"\tFetching failed! Status code {r.status_code}\n")
            continue

        with open(os.path.join(SAVED_DATA_FOLDER, url["name"]), "w") as d:
            d.write(r.text)

        print("\tSaved data!\n")

    print("Finished fetching data!\n")
