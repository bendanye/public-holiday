from datetime import datetime

from dataclasses import dataclass, field


@dataclass()
class PublicHoliday:
    name: str
    date: str
    day: str
    date_obj: datetime.date = field(init=False, repr=False)

    def __post_init__(self):
        self.date_obj = datetime.strptime(self.date, "%Y-%m-%d").date()

    def is_sunday(self):
        return "Sunday" == self.day

    def is_after(self, specified_date: datetime.date) -> bool:
        return specified_date < self.date_obj

    def __str__(self) -> str:
        return f"{self.name} - {self.date} ({self.day})"

    @staticmethod
    def dict_factory(x):
        exclude_fields = ["date_obj"]
        return {k: v for (k, v) in x if ((v is not None) and (k not in exclude_fields))}
