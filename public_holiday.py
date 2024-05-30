from dataclasses import dataclass


@dataclass(frozen=True)
class PublicHoliday:
    name: str
    date: str
    day: str

    def is_sunday(self):
        return "Sunday" == self.day
