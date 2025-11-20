import reflex as rx
import logging
from .athletes import AthleteState
from .settings import SettingsState
from ..models import Athlete


class IDCardState(rx.State):
    selected_athlete_idx: int = 0

    @rx.var
    async def selected_athlete(self) -> Athlete:
        athlete_state = await self.get_state(AthleteState)
        if 0 <= self.selected_athlete_idx < len(athlete_state.athletes):
            return athlete_state.athletes[self.selected_athlete_idx]
        return Athlete(first_name="Unknown", last_name="Student", belt_rank_id=0)

    @rx.var
    async def club_name(self) -> str:
        settings = await self.get_state(SettingsState)
        return settings.club_name

    @rx.var
    async def qr_code_url(self) -> str:
        athlete_state = await self.get_state(AthleteState)
        if 0 <= self.selected_athlete_idx < len(athlete_state.athletes):
            athlete = athlete_state.athletes[self.selected_athlete_idx]
            data = f"ID:{self.selected_athlete_idx}|{athlete.first_name} {athlete.last_name}"
            return (
                f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={data}"
            )
        return ""

    @rx.event
    def set_athlete_index(self, value: str):
        try:
            self.selected_athlete_idx = int(value)
        except ValueError as e:
            logging.exception(f"Error converting athlete index: {e}")
            pass

    @rx.event
    def print_card(self):
        return rx.window_alert("Sending to printer... (Simulated)")