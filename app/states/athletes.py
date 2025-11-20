import reflex as rx
from datetime import datetime
from ..models import Athlete
from .belts import BeltState


class AthleteState(rx.State):
    athletes: list[Athlete] = [
        Athlete(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="123456789",
            belt_rank_id=1,
            gender="Male",
            notes="Promising student",
        ),
        Athlete(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            phone="987654321",
            belt_rank_id=2,
            gender="Female",
        ),
    ]
    current_athlete: Athlete = Athlete(first_name="", last_name="", belt_rank_id=1)
    search_query: str = ""
    is_open: bool = False

    @rx.var
    def filtered_athletes(self) -> list[Athlete]:
        """Filter athletes by search query."""
        if not self.search_query:
            return self.athletes
        query = self.search_query.lower()
        return [
            a
            for a in self.athletes
            if query in a.first_name.lower() or query in a.last_name.lower()
        ]

    @rx.event
    def add_athlete(self):
        """Add a new athlete."""
        if not self.current_athlete.first_name or not self.current_athlete.last_name:
            return rx.toast.error("First and Last name are required")
        self.athletes.append(self.current_athlete)
        self.current_athlete = Athlete(first_name="", last_name="", belt_rank_id=1)
        self.is_open = False
        return rx.toast.success("Athlete registered successfully")

    @rx.event
    def delete_athlete(self, idx: int):
        """Delete an athlete."""
        if 0 <= idx < len(self.athletes):
            self.athletes.pop(idx)
            return rx.toast.info("Athlete deleted")

    @rx.event
    def set_field(self, field: str, value: str):
        setattr(self.current_athlete, field, value)

    @rx.event
    def set_search(self, value: str):
        self.search_query = value

    @rx.event
    def open_dialog(self):
        self.is_open = True

    @rx.event
    def close_dialog(self):
        self.is_open = False