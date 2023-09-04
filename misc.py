import json
from typing import TypedDict

from settings import SAVED_URLS_FILE


class _SavedUrlsEntry(TypedDict):
    name: str
    url: str


def get_answer(question: str) -> bool:
    while True:
        correct = input(f"{question} (Y/n) ").strip()

        if correct == "Y" or correct == "y":
            print()
            return True
        elif correct == "N" or correct == "n":
            print()
            return False
        elif correct == "":
            print()
            return True
        else:
            print("Please enter a valid character.")


def save_url(url: str, name: str):
    with open(SAVED_URLS_FILE, "r") as d:
        existing: list[_SavedUrlsEntry] = json.load(d)

    for entry in existing:
        if entry["name"] == name:
            print(f"The name '{name}' already exists!\n")
            return

    existing.append({"url": url, "name": name})

    with open(SAVED_URLS_FILE, "w") as d:
        json.dump(existing, d)

    print("The URL was successfully saved!\n")


def delete_url(index: int):
    with open(SAVED_URLS_FILE, "r") as d:
        existing: list[_SavedUrlsEntry] = json.load(d)

    existing.pop(index)

    with open(SAVED_URLS_FILE, "w") as d:
        json.dump(existing, d)

    print("The URL was successfully removed!\n")


def get_urls() -> list[_SavedUrlsEntry]:
    with open(SAVED_URLS_FILE, "r") as d:
        return json.load(d)
