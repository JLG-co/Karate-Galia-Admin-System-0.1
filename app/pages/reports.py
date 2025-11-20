import reflex as rx
from ..states.reports import ReportState


def report_summary_card(title: str, value: str, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name=f"h-6 w-6 text-{color}-600"),
                class_name=f"p-3 bg-{color}-100 rounded-full mr-4",
            ),
            rx.el.div(
                rx.el.p(title, class_name="text-sm text-gray-500 font-medium"),
                rx.el.p(value, class_name="text-2xl font-bold text-gray-900"),
            ),
            class_name="flex items-center",
        ),
        class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-200",
    )


def reports_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Reports & Analytics", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("General Overview", value="general"),
                    rx.el.option("Financial Report", value="financial"),
                    rx.el.option("Attendance Report", value="attendance"),
                    rx.el.option("Athlete Progress", value="progress"),
                    value=ReportState.report_type,
                    on_change=ReportState.set_report_type,
                    class_name="px-4 py-2 border rounded-lg mr-4",
                ),
                rx.el.button(
                    rx.icon("file-down", class_name="h-4 w-4 mr-2"),
                    "Export CSV",
                    on_click=ReportState.export_csv,
                    class_name="flex items-center px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors mr-2",
                ),
                rx.el.button(
                    rx.icon("file-text", class_name="h-4 w-4 mr-2"),
                    "Export PDF",
                    on_click=ReportState.export_pdf,
                    class_name="flex items-center px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors",
                ),
                class_name="flex items-center",
            ),
            class_name="flex justify-between items-center mb-8",
        ),
        rx.el.div(
            report_summary_card(
                "Total Athletes",
                ReportState.total_athletes.to_string(),
                "users",
                "blue",
            ),
            report_summary_card(
                "Active Students",
                ReportState.active_students.to_string(),
                "user-check",
                "green",
            ),
            report_summary_card(
                "Total Revenue",
                ReportState.total_revenue.to_string(),
                "dollar-sign",
                "yellow",
            ),
            report_summary_card("Classes Held", "24", "calendar", "purple"),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.h3(
                f"{ReportState.report_type.capitalize()} Report Preview",
                class_name="text-lg font-semibold text-gray-900 mb-4",
            ),
            rx.el.div(
                rx.el.p(
                    "Select a report type and click export to download the full detailed analysis.",
                    class_name="text-gray-500 text-center py-12",
                ),
                class_name="bg-white border border-gray-200 border-dashed rounded-xl p-8",
            ),
            class_name="mb-8",
        ),
    )