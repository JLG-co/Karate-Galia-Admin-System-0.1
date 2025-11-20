import reflex as rx
from ..models import Coach


class CoachState(rx.State):
    coaches: list[Coach] = [
        Coach(
            first_name="Sensei",
            last_name="Miyagi",
            specialty="Defense",
            phone="555-0199",
        ),
        Coach(
            first_name="Johnny",
            last_name="Lawrence",
            specialty="Offense",
            phone="555-0100",
        ),
    ]
    current_coach: Coach = Coach(first_name="", last_name="")
    is_open: bool = False

    @rx.event
    def add_coach(self):
        if not self.current_coach.first_name:
            return rx.toast.error("Name is required")
        self.coaches.append(self.current_coach)
        self.current_coach = Coach(first_name="", last_name="")
        self.is_open = False
        return rx.toast.success("Coach added successfully")

    @rx.event
    def delete_coach(self, idx: int):
        self.coaches.pop(idx)
        return rx.toast.info("Coach deleted")

    @rx.event
    def set_field(self, field: str, value: str):
        setattr(self.current_coach, field, value)

    @rx.event
    def open_dialog(self):
        self.is_open = True

    @rx.event
    def close_dialog(self):
        self.is_open = False