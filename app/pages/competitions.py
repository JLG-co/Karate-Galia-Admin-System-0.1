import reflex as rx
from ..states.competitions import CompetitionState


def competition_row(comp: rx.Var, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.p(comp.name, class_name="text-sm font-medium text-gray-900"),
                rx.el.p(comp.description, class_name="text-xs text-gray-500"),
                class_name="flex flex-col",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            comp.date.to_string(),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            comp.location,
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(f"${comp.fee}", class_name="font-bold text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    "trash-2", class_name="h-4 w-4 text-red-500 hover:text-red-700"
                ),
                on_click=lambda: CompetitionState.delete_competition(index),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def competitions_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Competitions", class_name="text-2xl font-bold text-gray-900"),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.el.button(
                        rx.icon("plus", class_name="h-4 w-4 mr-2"),
                        "New Competition",
                        class_name="flex items-center px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors",
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title("Add New Competition"),
                    rx.el.div(
                        rx.el.label(
                            "Event Name",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="Tournament Name",
                            on_change=lambda v: CompetitionState.set_field("name", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Date",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            type="date",
                            on_change=lambda v: CompetitionState.set_field("date", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Location",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="Venue Address",
                            on_change=lambda v: CompetitionState.set_field(
                                "location", v
                            ),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Registration Fee",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            type="number",
                            placeholder="0.00",
                            on_change=lambda v: CompetitionState.set_field("fee", v),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Description",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.textarea(
                            placeholder="Additional details...",
                            on_change=lambda v: CompetitionState.set_field(
                                "description", v
                            ),
                            class_name="w-full p-2 border rounded mb-4 h-24",
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
                            "Save Competition",
                            on_click=CompetitionState.add_competition,
                            class_name="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700",
                        ),
                        class_name="flex justify-end mt-4",
                    ),
                ),
                open=CompetitionState.is_open,
                on_open_change=CompetitionState.set_is_open,
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Event",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Location",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Fee",
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
                        CompetitionState.competitions,
                        lambda c, i: competition_row(c, i),
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200",
        ),
    )