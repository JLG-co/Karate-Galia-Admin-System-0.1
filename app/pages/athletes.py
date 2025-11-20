import reflex as rx
from ..states.athletes import AthleteState


def athlete_row(athlete: rx.Var, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        f"{athlete.first_name} {athlete.last_name}",
                        class_name="text-sm font-medium text-gray-900",
                    ),
                    rx.el.p(athlete.email, class_name="text-sm text-gray-500"),
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            athlete.gender,
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            athlete.phone,
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                "Active",
                class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    "trash-2", class_name="h-4 w-4 text-red-500 hover:text-red-700"
                ),
                on_click=lambda: AthleteState.delete_athlete(index),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def athletes_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Athletes", class_name="text-2xl font-bold text-gray-900"),
            rx.el.div(
                rx.el.input(
                    placeholder="Search athletes...",
                    on_change=AthleteState.set_search,
                    class_name="px-4 py-2 border rounded-lg mr-4 focus:ring-2 focus:ring-red-500 outline-none",
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.el.button(
                            rx.icon("user-plus", class_name="h-4 w-4 mr-2"),
                            "New Athlete",
                            class_name="flex items-center px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors",
                        )
                    ),
                    rx.dialog.content(
                        rx.dialog.title("Register New Athlete"),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "First Name",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="First Name",
                                    on_change=lambda v: AthleteState.set_field(
                                        "first_name", v
                                    ),
                                    class_name="w-full p-2 border rounded",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Last Name",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="Last Name",
                                    on_change=lambda v: AthleteState.set_field(
                                        "last_name", v
                                    ),
                                    class_name="w-full p-2 border rounded",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Email",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="email@example.com",
                                    on_change=lambda v: AthleteState.set_field(
                                        "email", v
                                    ),
                                    class_name="w-full p-2 border rounded",
                                ),
                                class_name="mb-4",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Phone",
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    placeholder="Phone Number",
                                    on_change=lambda v: AthleteState.set_field(
                                        "phone", v
                                    ),
                                    class_name="w-full p-2 border rounded",
                                ),
                                class_name="mb-4",
                            ),
                            class_name="py-4 grid grid-cols-2 gap-4",
                        ),
                        rx.el.div(
                            rx.dialog.close(
                                rx.el.button(
                                    "Cancel",
                                    class_name="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded mr-2",
                                )
                            ),
                            rx.el.button(
                                "Register Athlete",
                                on_click=AthleteState.add_athlete,
                                class_name="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700",
                            ),
                            class_name="flex justify-end mt-4",
                        ),
                    ),
                    open=AthleteState.is_open,
                    on_open_change=AthleteState.set_is_open,
                ),
                class_name="flex",
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
                            "Gender",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Phone",
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
                    rx.foreach(
                        AthleteState.filtered_athletes, lambda a, i: athlete_row(a, i)
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200",
        ),
    )