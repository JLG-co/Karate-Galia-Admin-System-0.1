import reflex as rx
from ..states.payments import PaymentState


def payment_row(payment: rx.Var, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(
                payment.payment_type,
                class_name="px-2 py-1 rounded bg-gray-100 text-gray-700 text-sm font-medium",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(f"DA {payment.amount}", class_name="font-bold text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            payment.payment_date.to_string(),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.cond(
                payment.status == "completed",
                rx.el.span(
                    "Paid",
                    class_name="text-green-600 bg-green-100 px-2 py-1 rounded text-xs font-bold uppercase",
                ),
                rx.el.span(
                    "Pending",
                    class_name="text-yellow-600 bg-yellow-100 px-2 py-1 rounded text-xs font-bold uppercase",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    "trash-2", class_name="h-4 w-4 text-red-500 hover:text-red-700"
                ),
                on_click=lambda: PaymentState.delete_payment(index),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def payments_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Payments", class_name="text-2xl font-bold text-gray-900"),
                rx.el.p(
                    f"Total Revenue: DA {PaymentState.total_income}",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.el.button(
                        rx.icon("banknote", class_name="h-4 w-4 mr-2"),
                        "New Payment",
                        class_name="flex items-center px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors",
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title("Record Payment"),
                    rx.el.div(
                        rx.el.label(
                            "Amount (DA)",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            type="number",
                            placeholder="500",
                            on_change=lambda v: PaymentState.set_field("amount", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Type",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.select(
                            rx.el.option("Monthly Fee", value="Monthly Fee"),
                            rx.el.option("Yearly License", value="Yearly License"),
                            rx.el.option("Gear Purchase", value="Gear Purchase"),
                            on_change=lambda v: PaymentState.set_field(
                                "payment_type", v
                            ),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Status",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.select(
                            rx.el.option("Completed", value="completed"),
                            rx.el.option("Pending", value="pending"),
                            on_change=lambda v: PaymentState.set_field("status", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        class_name="py-4",
                    ),
                    rx.el.div(
                        rx.dialog.close(
                            rx.el.button(
                                "Cancel",
                                class_name="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded mr-2",
                            )
                        ),
                        rx.el.button(
                            "Record Payment",
                            on_click=PaymentState.add_payment,
                            class_name="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700",
                        ),
                        class_name="flex justify-end mt-4",
                    ),
                ),
                open=PaymentState.is_open,
                on_open_change=PaymentState.set_is_open,
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Type",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Amount",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50",
                ),
                rx.el.tbody(
                    rx.foreach(PaymentState.payments, lambda p, i: payment_row(p, i)),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200",
        ),
    )