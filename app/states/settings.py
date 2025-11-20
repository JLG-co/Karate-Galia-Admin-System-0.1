import reflex as rx
import json
import logging
from datetime import datetime


class SettingsState(rx.State):
    club_name: str = "Cobra Kai Dojo"
    head_sensei: str = "Johnny Lawrence"
    monthly_fee: float = 500.0
    yearly_fee: float = 3000.0
    currency: str = "DA"
    language: str = "English"
    dark_mode: bool = False
    last_backup: str = "Never"

    @rx.event
    def update_setting(self, field: str, value: str):
        if field in ["monthly_fee", "yearly_fee"]:
            try:
                value = float(value)
            except ValueError as e:
                logging.exception(f"Error converting setting {field} to float: {e}")
                return
        setattr(self, field, value)
        return rx.toast.success(f"Updated {field.replace('_', ' ')}")

    @rx.event
    def toggle_dark_mode(self, value: bool):
        self.dark_mode = value
        mode = "Dark" if value else "Light"
        return rx.toast.info(f"{mode} mode enabled (Simulation)")

    @rx.event
    def create_backup(self):
        """Simulate a database backup operation."""
        self.last_backup = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return rx.toast.success("System backup created successfully")

    @rx.event
    def restore_backup(self):
        """Simulate a restore operation."""
        return rx.toast.info("Restore feature is simulated for this demo")