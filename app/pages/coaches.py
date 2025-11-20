import reflex as rx
from ..states.coaches import CoachState


def coach_row(coach: rx.Var, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        f"{coach.first_name} {coach.last_name}",
                        class_name="text-sm font-medium text-gray-900",
                    ),
                    rx.el.p(coach.specialty, class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            coach.phone, class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
        ),
        rx.el.td(
            coach.bio, class_name="px-6 py-4 text-sm text-gray-500 max-w-xs truncate"
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    "trash-2", class_name="h-4 w-4 text-red-500 hover:text-red-700"
                ),
                on_click=lambda: CoachState.delete_coach(index),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def coaches_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Coaches", class_name="text-2xl font-bold text-gray-900"),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.el.button(
                        rx.icon("plus", class_name="h-4 w-4 mr-2"),
                        "New Coach",
                        class_name="flex items-center px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors",
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title("Add New Coach"),
                    rx.el.div(
                        rx.el.label(
                            "First Name",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="First Name",
                            on_change=lambda v: CoachState.set_field("first_name", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Last Name",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="Last Name",
                            on_change=lambda v: CoachState.set_field("last_name", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Specialty",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="e.g. Kata, Kumite",
                            on_change=lambda v: CoachState.set_field("specialty", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Phone",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="Phone Number",
                            on_change=lambda v: CoachState.set_field("phone", v),
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
                            "Save Coach",
                            on_click=CoachState.add_coach,
                            class_name="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700",
                        ),
                        class_name="flex justify-end mt-4",
                    ),
                ),
                open=CoachState.is_open,
                on_open_change=CoachState.set_is_open,
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Phone",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Bio/Notes",
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
                    rx.foreach(CoachState.coaches, lambda c, i: coach_row(c, i)),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200",
        ),
    )