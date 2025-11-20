import reflex as rx
from datetime import datetime
from ..models import Attendance
from .athletes import AthleteState


class AttendanceState(rx.State):
    selected_date: str = datetime.now().strftime("%Y-%m-%d")
    records: list[Attendance] = []

    @rx.event
    def set_date(self, date_str: str):
        self.selected_date = date_str

    @rx.event
    def mark_status(self, athlete_id: int, status: str):
        self.records = [
            r
            for r in self.records
            if not (
                r.athlete_id == athlete_id
                and r.date.strftime("%Y-%m-%d") == self.selected_date
            )
        ]
        new_record = Attendance(
            athlete_id=athlete_id,
            status=status,
            date=datetime.strptime(self.selected_date, "%Y-%m-%d"),
        )
        self.records.append(new_record)

    @rx.event
    def get_status(self, athlete_id: int) -> str:
        pass