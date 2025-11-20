import reflex as rx
from .sidebar import sidebar
from ..states.auth import AuthState


def layout(content: rx.Component) -> rx.Component:
    """Main layout with sidebar and content area."""
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.header(
                rx.el.div(
                    rx.el.h2(
                        "Karate Manager",
                        class_name="text-xl font-semibold text-gray-800",
                    ),
                    rx.el.div(
                        rx.el.span(
                            rx.moment(format="MMMM Do YYYY"),
                            class_name="text-sm text-gray-500 font-medium",
                        ),
                        class_name="flex items-center",
                    ),
                    class_name="flex justify-between items-center h-16 px-8 bg-white border-b border-gray-200",
                )
            ),
            rx.el.div(
                content,
                class_name="p-8 overflow-y-auto h-[calc(100vh-64px)] bg-gray-50",
            ),
            class_name="ml-64 min-h-screen flex flex-col w-[calc(100%-16rem)]",
        ),
        class_name="flex min-h-screen bg-gray-50 font-['Inter']",
    )


def require_auth(page: rx.Component) -> rx.Component:
    """Decorator-like function to protect routes."""
    return rx.cond(
        AuthState.is_authenticated,
        layout(page),
        rx.el.div(
            rx.el.div("Redirecting to login...", class_name="text-gray-500"),
            rx.el.script("setTimeout(() => { window.location.href = '/login' }, 100)"),
            class_name="flex items-center justify-center h-screen",
        ),
    )