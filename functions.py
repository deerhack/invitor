import csv
from typing import List
from person import Person
import uuid

FILE_PATH = "participants.csv"
filed_names = ["first_name", "last_name", "email", "team"]


def get_participants() -> List[Person]:
    with open(FILE_PATH, "r", newline="") as reader:
        reader = csv.DictReader(
            reader,
            fieldnames=filed_names,
        )
        persons: List[Person] = []
        for row in reader:
            # print(row["first_name"])
            if row["first_name"] == "first_name":
                continue
            person = Person(
                uuid=str(uuid.uuid4()),
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                team=None,
            )
            persons.append(person)
    return persons
