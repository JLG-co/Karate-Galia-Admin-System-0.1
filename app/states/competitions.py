import reflex as rx
import logging
from datetime import datetime
from ..models import Competition


class CompetitionState(rx.State):
    competitions: list[Competition] = [
        Competition(
            name="All Valley Tournament",
            date=datetime(2023, 12, 15),
            location="Reseda, CA",
            description="Annual under-18 karate championship",
            fee=50.0,
        ),
        Competition(
            name="Regional Qualifier",
            date=datetime(2024, 3, 10),
            location="West Valley High",
            description="Qualifier for state finals",
            fee=30.0,
        ),
    ]
    current_competition: Competition = Competition(
        name="", date=datetime.now(), location=""
    )
    is_open: bool = False

    @rx.event
    def add_competition(self):
        if not self.current_competition.name:
            return rx.toast.error("Competition name is required")
        if not isinstance(self.current_competition.date, datetime):
            self.current_competition.date = datetime.now()
        self.competitions.append(self.current_competition)
        self.current_competition = Competition(
            name="", date=datetime.now(), location=""
        )
        self.is_open = False
        return rx.toast.success("Competition added successfully")

    @rx.event
    def delete_competition(self, idx: int):
        if 0 <= idx < len(self.competitions):
            self.competitions.pop(idx)
            return rx.toast.info("Competition deleted")

    @rx.event
    def set_field(self, field: str, value: str):
        if field == "fee":
            try:
                value = float(value)
            except ValueError as e:
                logging.exception(f"Error converting fee to float: {e}")
                value = 0.0
        elif field == "date":
            try:
                value = datetime.strptime(value, "%Y-%m-%d")
            except ValueError as e:
                logging.exception(f"Error parsing date: {e}")
                pass
        setattr(self.current_competition, field, value)

    @rx.event
    def open_dialog(self):
        self.is_open = True

    @rx.event
    def close_dialog(self):
        self.is_open = False