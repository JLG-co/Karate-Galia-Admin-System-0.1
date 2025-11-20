import reflex as rx
from ..states.settings import SettingsState


def settings_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("System Settings", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Club Information",
                    class_name="text-lg font-semibold text-gray-900 mb-4 border-b pb-2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Dojo Name",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            on_change=lambda v: SettingsState.update_setting(
                                "club_name", v
                            ),
                            class_name="w-full p-2 border rounded",
                            default_value=SettingsState.club_name,
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Head Instructor",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            on_change=lambda v: SettingsState.update_setting(
                                "head_sensei", v
                            ),
                            class_name="w-full p-2 border rounded",
                            default_value=SettingsState.head_sensei,
                        ),
                        class_name="mb-4",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-200 mb-6",
            ),
            rx.el.div(
                rx.el.h3(
                    "Financial Settings",
                    class_name="text-lg font-semibold text-gray-900 mb-4 border-b pb-2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Monthly Fee",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.div(
                            rx.el.span(
                                SettingsState.currency,
                                class_name="px-3 py-2 bg-gray-100 border border-r-0 rounded-l text-gray-500",
                            ),
                            rx.el.input(
                                on_change=lambda v: SettingsState.update_setting(
                                    "monthly_fee", v
                                ),
                                class_name="w-full p-2 border rounded-r",
                                default_value=SettingsState.monthly_fee.to_string(),
                            ),
                            class_name="flex",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Yearly License",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.div(
                            rx.el.span(
                                SettingsState.currency,
                                class_name="px-3 py-2 bg-gray-100 border border-r-0 rounded-l text-gray-500",
                            ),
                            rx.el.input(
                                on_change=lambda v: SettingsState.update_setting(
                                    "yearly_fee", v
                                ),
                                class_name="w-full p-2 border rounded-r",
                                default_value=SettingsState.yearly_fee.to_string(),
                            ),
                            class_name="flex",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Currency Symbol",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            on_change=lambda v: SettingsState.update_setting(
                                "currency", v
                            ),
                            class_name="w-full p-2 border rounded",
                            default_value=SettingsState.currency,
                        ),
                        class_name="mb-4",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-4",
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-200 mb-6",
            ),
            rx.el.div(
                rx.el.h3(
                    "Preferences & Backup",
                    class_name="text-lg font-semibold text-gray-900 mb-4 border-b pb-2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Language",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.select(
                            rx.el.option("English", value="English"),
                            rx.el.option("French", value="French"),
                            rx.el.option("Arabic", value="Arabic"),
                            value=SettingsState.language,
                            on_change=lambda v: SettingsState.update_setting(
                                "language", v
                            ),
                            class_name="w-full p-2 border rounded",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Theme",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                rx.el.input(
                                    type="checkbox",
                                    checked=SettingsState.dark_mode,
                                    on_change=SettingsState.toggle_dark_mode,
                                    class_name="mr-2 h-4 w-4",
                                ),
                                "Enable Dark Mode (Preview)",
                                class_name="flex items-center",
                            ),
                            class_name="p-2",
                        ),
                        class_name="mb-4",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            f"Last Backup: {SettingsState.last_backup}",
                            class_name="text-sm text-gray-500 mb-2",
                        ),
                        rx.el.div(
                            rx.el.button(
                                rx.icon("download", class_name="h-4 w-4 mr-2"),
                                "Backup Database",
                                on_click=SettingsState.create_backup,
                                class_name="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors mr-3",
                            ),
                            rx.el.button(
                                rx.icon("upload", class_name="h-4 w-4 mr-2"),
                                "Restore Backup",
                                on_click=SettingsState.restore_backup,
                                class_name="flex items-center px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors",
                            ),
                            class_name="flex",
                        ),
                        class_name="mt-4 pt-4 border-t border-gray-100",
                    ),
                    class_name="",
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-200 mb-6",
            ),
        ),
    )