import reflex as rx
from typing import Optional
from ..models import User


class AuthState(rx.State):
    username: str = ""
    password: str = ""
    user: Optional[User] = None
    is_authenticated: bool = False
    _redirect_to: str = "/dashboard"

    @rx.event
    def logout(self):
        """Log the user out and redirect to login."""
        self.user = None
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        return rx.redirect("/login")

    @rx.event
    def login(self, form_data: dict):
        """Handle login logic."""
        username = form_data.get("username")
        password = form_data.get("password")
        if username == "admin" and password == "admin":
            self.user = User(
                username="admin",
                role="admin",
                full_name="Sensei Admin",
                email="admin@dojo.com",
                password_hash="mock_hash",
            )
            self.is_authenticated = True
            return rx.redirect(self._redirect_to)
        return rx.window_alert("Invalid credentials. Try admin/admin")

    @rx.var
    def user_full_name(self) -> str:
        if not self.user:
            return "Guest"
        if isinstance(self.user, dict):
            return self.user.get("full_name", "Guest")
        return self.user.full_name

    @rx.var
    def user_role(self) -> str:
        if not self.user:
            return ""
        if isinstance(self.user, dict):
            return self.user.get("role", "")
        return self.user.role