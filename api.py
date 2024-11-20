from typing import List

import requests
import datetime
import json

from dataclasses import asdict
from public_holiday import PublicHoliday


def get_singapore_public_holiday(year: int, resouce_id: str) -> List[PublicHoliday]:
    base_url = "https://data.gov.sg/api/action/datastore_search"
    url = base_url + f"?resource_id={resouce_id}"
    response = requests.get(url)
    records = response.json()["result"]["records"]

    result = []
    for record in records:
        ph = PublicHoliday(
            name=record["holiday"], date=record["date"], day=record["day"]
        )
        result.append(ph)
        if ph.is_sunday():
            current_day = datetime.datetime.strptime(ph.date, "%Y-%m-%d")
            next_day = current_day + datetime.timedelta(days=1)
            result.append(
                PublicHoliday(
                    name=record["holiday"],
                    date=next_day.strftime("%Y-%m-%d"),
                    day="Monday",
                )
            )

    return result


def save_as_json(year: int, country: str, records: List[PublicHoliday]) -> None:
    data_dict_list = [
        asdict(item, dict_factory=PublicHoliday.dict_factory) for item in records
    ]
    with open(f"{year}_{country}_ph.json", "w") as f:
        json.dump(data_dict_list, f, indent=4)


if __name__ == "__main__":
    year = 2025
    resource_id = "d_3751791452397f1b1c80c451447e40b7"
    singapore_ph_records = get_singapore_public_holiday(year, resource_id)
    save_as_json(year, "singapore", singapore_ph_records)
