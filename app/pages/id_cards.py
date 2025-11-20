import reflex as rx
from ..states.id_cards import IDCardState
from ..states.athletes import AthleteState


def id_card_preview() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("sword", class_name="h-8 w-8 text-white"),
                rx.el.div(
                    rx.el.h2(
                        IDCardState.club_name,
                        class_name="text-xl font-bold text-white uppercase tracking-wider",
                    ),
                    rx.el.p(
                        "Official Athlete ID",
                        class_name="text-xs text-red-100 uppercase",
                    ),
                    class_name="ml-3",
                ),
                class_name="bg-red-700 p-4 flex items-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("user", class_name="h-16 w-16 text-gray-400"),
                        class_name="h-24 w-24 bg-gray-100 rounded-lg flex items-center justify-center border border-gray-200",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            f"{IDCardState.selected_athlete.first_name} {IDCardState.selected_athlete.last_name}",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        rx.el.p(
                            "Athlete",
                            class_name="text-sm font-medium text-gray-500 uppercase mt-1",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "Status:", class_name="text-xs text-gray-400 mr-1"
                            ),
                            rx.el.span(
                                "Active",
                                class_name="text-xs font-bold text-green-600 uppercase",
                            ),
                            class_name="mt-2",
                        ),
                        class_name="ml-4 flex-1",
                    ),
                    class_name="flex items-start p-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Scan for record",
                            class_name="text-xs text-gray-400 mb-1 text-center",
                        ),
                        rx.image(
                            src=IDCardState.qr_code_url,
                            class_name="h-20 w-20 mix-blend-multiply",
                        ),
                        class_name="flex flex-col items-center",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Valid Thru",
                                class_name="text-xs text-gray-400 uppercase",
                            ),
                            rx.el.p("Dec 2024", class_name="font-bold text-gray-900"),
                            class_name="mb-2",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Belt Rank",
                                class_name="text-xs text-gray-400 uppercase",
                            ),
                            rx.el.p("Student", class_name="font-bold text-gray-900"),
                        ),
                        class_name="ml-auto text-right",
                    ),
                    class_name="flex justify-between items-end p-6 pt-0",
                ),
                class_name="bg-white",
            ),
            class_name="w-[400px] overflow-hidden rounded-xl shadow-lg border border-gray-200 print:shadow-none print:border-black",
        ),
        class_name="flex justify-center p-8",
    )


def id_cards_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Athlete ID Cards", class_name="text-2xl font-bold text-gray-900 mb-2"
            ),
            rx.el.p(
                "Generate and print ID cards with QR codes.",
                class_name="text-gray-500 mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Select Athlete",
                        class_name="block text-sm font-medium text-gray-700 mb-2",
                    ),
                    rx.el.select(
                        rx.foreach(
                            AthleteState.athletes,
                            lambda a, i: rx.el.option(
                                f"{a.first_name} {a.last_name}", value=i.to_string()
                            ),
                        ),
                        on_change=IDCardState.set_athlete_index,
                        class_name="w-full p-2 border rounded-lg mb-4",
                    ),
                    rx.el.button(
                        rx.icon("printer", class_name="h-4 w-4 mr-2"),
                        "Print Card",
                        on_click=IDCardState.print_card,
                        class_name="flex items-center justify-center w-full px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors",
                    ),
                    class_name="w-64 shrink-0 mr-8",
                ),
                rx.el.div(
                    id_card_preview(),
                    class_name="flex-1 bg-gray-100 rounded-xl border-2 border-dashed border-gray-300 flex items-center justify-center min-h-[400px]",
                ),
                class_name="flex flex-col md:flex-row items-start",
            ),
        )
    )