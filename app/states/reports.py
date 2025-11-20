import reflex as rx
from .athletes import AthleteState
from .payments import PaymentState
from .attendance import AttendanceState


class ReportState(rx.State):
    report_type: str = "general"

    @rx.var
    async def total_athletes(self) -> int:
        athlete_state = await self.get_state(AthleteState)
        return len(athlete_state.athletes)

    @rx.var
    async def total_revenue(self) -> float:
        payment_state = await self.get_state(PaymentState)
        return sum(
            (p.amount for p in payment_state.payments if p.status == "completed")
        )

    @rx.var
    async def active_students(self) -> int:
        athlete_state = await self.get_state(AthleteState)
        return len([a for a in athlete_state.athletes if a.is_active])

    @rx.event
    def set_report_type(self, value: str):
        self.report_type = value

    @rx.event
    def export_csv(self):
        """Simulate CSV export."""
        return rx.toast.success(f"Exported {self.report_type} report to CSV")

    @rx.event
    def export_pdf(self):
        """Simulate PDF export."""
        return rx.toast.success(f"Exported {self.report_type} report to PDF")