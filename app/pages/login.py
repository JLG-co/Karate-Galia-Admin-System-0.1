import reflex as rx
from ..states.auth import AuthState


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("sword", class_name="h-24 w-24 text-white mb-6 opacity-90"),
                    rx.el.h1(
                        "Karate Manager",
                        class_name="text-4xl font-bold text-white mb-4 tracking-tight",
                    ),
                    rx.el.p(
                        "Manage your dojo with honor and precision.",
                        class_name="text-red-100 text-lg max-w-md text-center",
                    ),
                    class_name="flex flex-col items-center justify-center h-full p-12",
                ),
                class_name="hidden lg:block lg:w-1/2 bg-gradient-to-br from-red-700 to-red-900",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Welcome Back",
                            class_name="text-3xl font-bold text-gray-900 mb-2",
                        ),
                        rx.el.p(
                            "Please sign in to continue",
                            class_name="text-gray-500 mb-8",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Username",
                                class_name="block text-sm font-medium text-gray-700 mb-2",
                            ),
                            rx.el.input(
                                placeholder="Enter your username",
                                class_name="w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-red-500 focus:border-transparent outline-none transition-all",
                                name="username",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Password",
                                class_name="block text-sm font-medium text-gray-700 mb-2",
                            ),
                            rx.el.input(
                                type="password",
                                placeholder="••••••••",
                                class_name="w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-red-500 focus:border-transparent outline-none transition-all",
                                name="password",
                            ),
                            class_name="mb-8",
                        ),
                        rx.el.button(
                            "Sign In",
                            type="submit",
                            class_name="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-3.5 rounded-lg transition-colors duration-200 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5",
                        ),
                        on_submit=AuthState.login,
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Demo Credentials: admin / admin",
                            class_name="text-center text-sm text-gray-400 mt-8",
                        )
                    ),
                    class_name="w-full max-w-md",
                ),
                class_name="w-full lg:w-1/2 flex items-center justify-center p-8 bg-white",
            ),
            class_name="flex w-full max-w-6xl h-[800px] bg-white rounded-2xl shadow-2xl overflow-hidden",
        ),
        class_name="min-h-screen w-full bg-gray-100 flex items-center justify-center p-4 font-['Inter']",
    )