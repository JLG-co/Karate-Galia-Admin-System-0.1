import reflex as rx
from .pages.login import login_page
from .pages.dashboard import dashboard
from .pages.athletes import athletes_page
from .pages.coaches import coaches_page
from .pages.belts import belts_page
from .pages.payments import payments_page
from .pages.attendance import attendance_page
from .components.layout import require_auth


def index() -> rx.Component:
    return rx.el.div(rx.el.script("window.location.href = '/login'"))


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(login_page, route="/login")
app.add_page(lambda: require_auth(dashboard()), route="/dashboard")
app.add_page(lambda: require_auth(athletes_page()), route="/athletes")
app.add_page(lambda: require_auth(coaches_page()), route="/coaches")
app.add_page(lambda: require_auth(belts_page()), route="/belts")
app.add_page(lambda: require_auth(payments_page()), route="/payments")
app.add_page(lambda: require_auth(attendance_page()), route="/attendance")
from .pages.competitions import competitions_page
from .pages.reports import reports_page
from .pages.settings import settings_page
from .pages.id_cards import id_cards_page

app.add_page(lambda: require_auth(competitions_page()), route="/competitions")
app.add_page(lambda: require_auth(reports_page()), route="/reports")
app.add_page(lambda: require_auth(settings_page()), route="/settings")
app.add_page(lambda: require_auth(id_cards_page()), route="/id-cards")