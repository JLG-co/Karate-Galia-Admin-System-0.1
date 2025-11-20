import reflex as rx
from ..states.auth import AuthState


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(
                icon,
                class_name="h-5 w-5 text-gray-400 group-hover:text-red-500 transition-colors",
            ),
            rx.el.span(text, class_name="ml-3 font-medium"),
            class_name="flex items-center w-full p-3 rounded-lg hover:bg-gray-800 transition-all duration-200 group",
        ),
        href=url,
        class_name="w-full mb-1",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("sword", class_name="h-8 w-8 text-red-600"),
                rx.el.h1(
                    "DOJO",
                    class_name="text-2xl font-bold text-white tracking-wider ml-2",
                ),
                class_name="flex items-center justify-center mb-8 pt-4",
            ),
            class_name="h-20 flex items-center justify-center border-b border-gray-800",
        ),
        rx.el.nav(
            rx.el.div(
                rx.el.p(
                    "MAIN",
                    class_name="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2 mt-4",
                ),
                sidebar_item("Dashboard", "layout-dashboard", "/dashboard"),
                sidebar_item("Athletes", "users", "/athletes"),
                sidebar_item("Coaches", "dumbbell", "/coaches"),
            ),
            rx.el.div(
                rx.el.p(
                    "MANAGEMENT",
                    class_name="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2 mt-6",
                ),
                sidebar_item("Attendance", "calendar-check", "/attendance"),
                sidebar_item("Payments", "credit-card", "payments"),
                sidebar_item("Competitions", "trophy", "/competitions"),
                sidebar_item("Belts & Ranks", "medal", "/belts"),
                sidebar_item("Reports", "bar-chart-3", "/reports"),
                sidebar_item("ID Cards", "contact", "/id-cards"),
            ),
            rx.el.div(
                rx.el.p(
                    "SYSTEM",
                    class_name="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2 mt-6",
                ),
                sidebar_item("Settings", "settings", "/settings"),
            ),
            class_name="flex flex-col px-4 pb-4 overflow-y-auto flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="h-5 w-5 text-white"),
                    class_name="h-10 w-10 rounded-full bg-red-600 flex items-center justify-center shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        AuthState.user_full_name,
                        class_name="text-sm font-medium text-white truncate",
                    ),
                    rx.el.p(
                        AuthState.user_role,
                        class_name="text-xs text-gray-400 truncate capitalize",
                    ),
                    class_name="ml-3 flex-1 overflow-hidden",
                ),
                rx.el.button(
                    rx.icon(
                        "log-out", class_name="h-5 w-5 text-gray-400 hover:text-red-500"
                    ),
                    on_click=AuthState.logout,
                    class_name="ml-2 p-1 rounded hover:bg-gray-800",
                ),
                class_name="flex items-center w-full",
            ),
            class_name="p-4 border-t border-gray-800 mt-auto",
        ),
        class_name="w-64 bg-gray-900 flex flex-col h-screen fixed left-0 top-0 z-30 shadow-xl text-gray-300",
    )