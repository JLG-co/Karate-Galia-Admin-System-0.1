import reflex as rx


def stat_card(
    title: str, value: str, icon: str, trend: str, trend_up: bool
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(title, class_name="text-sm font-medium text-gray-500 mb-1"),
                rx.el.h3(value, class_name="text-2xl font-bold text-gray-900"),
            ),
            rx.el.div(
                rx.icon(icon, class_name="h-6 w-6 text-red-600"),
                class_name="h-12 w-12 rounded-full bg-red-50 flex items-center justify-center",
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.span(
                trend,
                class_name=f"text-sm font-medium {('text-green-600' if trend_up else 'text-red-600')}",
            ),
            rx.el.span(" vs last month", class_name="text-sm text-gray-400 ml-1"),
            class_name="flex items-center",
        ),
        class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200",
    )


def action_card(title: str, desc: str, icon: str, color: str) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.icon(icon, class_name=f"h-8 w-8 text-{color}-600 mb-4"),
            rx.el.h3(title, class_name="text-lg font-semibold text-gray-900 mb-2"),
            rx.el.p(desc, class_name="text-sm text-gray-500 text-left"),
        ),
        class_name=f"flex flex-col items-start p-6 bg-white rounded-xl shadow-sm border border-gray-100 hover:border-{color}-200 hover:shadow-md transition-all duration-200 group w-full",
    )


def dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Dashboard Overview", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.p(
                "Monitor your club's performance and growth.",
                class_name="text-gray-500 mt-1",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            stat_card("Total Athletes", "124", "users", "+12%", True),
            stat_card("Monthly Income", "DA 45k", "credit-card", "+8%", True),
            stat_card("Attendance Rate", "92%", "calendar-check", "-2%", False),
            stat_card("Belt Promotions", "15", "medal", "+5%", True),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Recent Activity", class_name="text-lg font-bold text-gray-900"
                    ),
                    rx.el.button(
                        "View All",
                        class_name="text-sm text-red-600 font-medium hover:text-red-700",
                    ),
                    class_name="flex justify-between items-center mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                class_name="h-2 w-2 rounded-full bg-green-500 mt-2"
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "New athlete registration: John Doe",
                                    class_name="text-sm font-medium text-gray-900",
                                ),
                                rx.el.p(
                                    "2 hours ago", class_name="text-xs text-gray-500"
                                ),
                                class_name="ml-3",
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="pb-4 border-b border-gray-50 mb-4 last:border-0 last:mb-0 last:pb-0",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                class_name="h-2 w-2 rounded-full bg-blue-500 mt-2"
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Payment received from Sarah Smith",
                                    class_name="text-sm font-medium text-gray-900",
                                ),
                                rx.el.p(
                                    "4 hours ago", class_name="text-xs text-gray-500"
                                ),
                                class_name="ml-3",
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="pb-4 border-b border-gray-50 mb-4 last:border-0 last:mb-0 last:pb-0",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                class_name="h-2 w-2 rounded-full bg-yellow-500 mt-2"
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Upcoming competition reminder sent",
                                    class_name="text-sm font-medium text-gray-900",
                                ),
                                rx.el.p(
                                    "1 day ago", class_name="text-xs text-gray-500"
                                ),
                                class_name="ml-3",
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="pb-4 border-b border-gray-50 mb-4 last:border-0 last:mb-0 last:pb-0",
                    ),
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
            ),
            rx.el.div(
                rx.el.h3(
                    "Quick Actions", class_name="text-lg font-bold text-gray-900 mb-6"
                ),
                rx.el.div(
                    action_card(
                        "New Athlete",
                        "Register a new student to the dojo",
                        "user-plus",
                        "red",
                    ),
                    action_card(
                        "Record Attendance",
                        "Mark today's class attendance",
                        "clipboard-check",
                        "blue",
                    ),
                    action_card(
                        "New Payment",
                        "Record a monthly or gear payment",
                        "banknote",
                        "green",
                    ),
                    class_name="grid grid-cols-1 gap-4",
                ),
                class_name="flex flex-col",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
        ),
    )