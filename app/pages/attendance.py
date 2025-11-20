import reflex as rx
from ..states.attendance import AttendanceState
from ..states.athletes import AthleteState


def attendance_row(athlete: rx.Var, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.p(
                    f"{athlete.first_name} {athlete.last_name}",
                    class_name="text-sm font-medium text-gray-900",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    "Present",
                    on_click=lambda: AttendanceState.mark_status(index, "present"),
                    class_name="px-3 py-1 bg-gray-100 hover:bg-green-100 text-green-700 rounded-l-lg text-xs font-semibold border border-gray-200",
                ),
                rx.el.button(
                    "Absent",
                    on_click=lambda: AttendanceState.mark_status(index, "absent"),
                    class_name="px-3 py-1 bg-gray-100 hover:bg-red-100 text-red-700 text-xs font-semibold border-t border-b border-gray-200",
                ),
                rx.el.button(
                    "Late",
                    on_click=lambda: AttendanceState.mark_status(index, "late"),
                    class_name="px-3 py-1 bg-gray-100 hover:bg-yellow-100 text-yellow-700 rounded-r-lg text-xs font-semibold border border-gray-200",
                ),
                class_name="flex",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
    )


def attendance_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Daily Attendance", class_name="text-2xl font-bold text-gray-900"),
            rx.el.input(
                type="date",
                on_change=AttendanceState.set_date,
                class_name="px-4 py-2 border rounded-lg shadow-sm",
                default_value=AttendanceState.selected_date,
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Athlete",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50",
                ),
                rx.el.tbody(
                    rx.foreach(
                        AthleteState.athletes, lambda a, i: attendance_row(a, i)
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200",
        ),
    )