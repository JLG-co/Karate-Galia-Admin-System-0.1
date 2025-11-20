import reflex as rx
import logging
from datetime import datetime
from ..models import Payment


class PaymentState(rx.State):
    payments: list[Payment] = [
        Payment(
            athlete_id=1, amount=500.0, payment_type="Monthly Fee", status="completed"
        ),
        Payment(athlete_id=2, amount=300.0, payment_type="License", status="pending"),
    ]
    current_payment: Payment = Payment(
        athlete_id=0, amount=500.0, payment_type="Monthly Fee"
    )
    is_open: bool = False

    @rx.var
    def total_income(self) -> float:
        return sum((p.amount for p in self.payments if p.status == "completed"))

    @rx.event
    def add_payment(self):
        self.payments.insert(0, self.current_payment)
        self.current_payment = Payment(
            athlete_id=0, amount=500.0, payment_type="Monthly Fee"
        )
        self.is_open = False
        return rx.toast.success("Payment recorded")

    @rx.event
    def delete_payment(self, idx: int):
        self.payments.pop(idx)
        return rx.toast.info("Payment deleted")

    @rx.event
    def set_field(self, field: str, value: str):
        if field == "amount":
            try:
                value = float(value)
            except ValueError as e:
                logging.exception(f"Error converting amount to float: {e}")
                value = 0.0
        setattr(self.current_payment, field, value)

    @rx.event
    def open_dialog(self):
        self.is_open = True

    @rx.event
    def close_dialog(self):
        self.is_open = False