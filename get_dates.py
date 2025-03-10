import json
import sys
import os

from datetime import date
from typing import List

from public_holiday import PublicHoliday

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))


def list_this_year_public_holiday(
    country: str, specified_date, displaycount: int = 20
) -> None:
    year = specified_date.year
    public_holidays = _load(year, country)
    filtered_holidays = _get_after_specified_date(public_holidays, specified_date)
    _display(filtered_holidays, displaycount)


def _load(year: int, country: str) -> List[PublicHoliday]:
    with open(f"{SCRIPT_DIR}/data/{year}/{year}_{country}_ph.json", "r") as f:
        records = json.load(f)
        return [
            PublicHoliday(name=record["name"], date=record["date"], day=record["day"])
            for record in records
        ]


def _display(public_holidays: List[PublicHoliday], display_count: int):
    current_count = 0
    for public_holiday in public_holidays:
        if current_count >= display_count:
            break

        print(public_holiday)
        current_count += 1


def _get_after_specified_date(
    public_holidays: List[PublicHoliday], specified_date
) -> List[PublicHoliday]:
    result = []
    for public_holiday in public_holidays:
        if public_holiday.is_after(specified_date):
            result.append(public_holiday)
    return result


if __name__ == "__main__":
    display_count = 20
    if len(sys.argv) == 2:
        display_count = int(sys.argv[1])

    list_this_year_public_holiday("singapore", date.today(), display_count)
