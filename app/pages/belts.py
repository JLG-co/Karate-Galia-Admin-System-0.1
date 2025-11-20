import reflex as rx
from ..states.belts import BeltState


def belt_row(belt: rx.Var, index: int) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                class_name="w-8 h-8 rounded-full border border-gray-200 shadow-sm",
                style={"backgroundColor": belt.color_hex},
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            belt.rank_order,
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            belt.name,
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            belt.description,
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    "trash-2", class_name="h-4 w-4 text-red-500 hover:text-red-700"
                ),
                on_click=lambda: BeltState.delete_belt(index),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
    )


def belts_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Belt Ranks", class_name="text-2xl font-bold text-gray-900"),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.el.button(
                        rx.icon("plus", class_name="h-4 w-4 mr-2"),
                        "Add Belt",
                        class_name="flex items-center px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors",
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title("Add New Belt Rank"),
                    rx.dialog.description("Define a new belt level for the dojo."),
                    rx.el.div(
                        rx.el.label(
                            "Rank Name",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            placeholder="e.g. Yellow Belt",
                            on_change=lambda v: BeltState.set_current_belt_field(
                                "name", v
                            ),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Rank Order",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            type="number",
                            placeholder="e.g. 1",
                            on_change=lambda v: BeltState.set_current_belt_field(
                                "rank_order", v
                            ),
                            class_name="w-full p-2 border rounded mb-4",
                        ),
                        rx.el.label(
                            "Color Hex",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            type="color",
                            on_change=lambda v: BeltState.set_current_belt_field(
                                "color_hex", v
                            ),
                            class_name="w-full h-10 p-1 border rounded mb-4",
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
                            "Save Belt",
                            on_click=BeltState.add_belt,
                            class_name="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700",
                        ),
                        class_name="flex justify-end mt-4",
                    ),
                ),
                open=BeltState.is_open,
                on_open_change=BeltState.set_is_open,
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Color",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Order",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Description",
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
                    rx.foreach(BeltState.belts, lambda b, i: belt_row(b, i)),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200",
        ),
    )