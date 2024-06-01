import json

from datetime import date
from typing import List

from public_holiday import PublicHoliday


def list_this_year_public_holiday(country: str, specified_date) -> None:
    year = specified_date.year
    public_holidays = _load(year, country)
    for public_holiday in _get_after_specified_date(public_holidays, specified_date):
        print(public_holiday)


def _load(year: int, country: str) -> List[PublicHoliday]:
    with open(f"data/{year}/{year}_{country}_ph.json", "r") as f:
        records = json.load(f)
        return [
            PublicHoliday(name=record["name"], date=record["date"], day=record["day"])
            for record in records
        ]


def _get_after_specified_date(
    public_holidays: List[PublicHoliday], specified_date
) -> List[PublicHoliday]:
    result = []
    for public_holiday in public_holidays:
        if public_holiday.is_after(specified_date):
            result.append(public_holiday)
    return result


if __name__ == "__main__":
    list_this_year_public_holiday("singapore", date.today())
