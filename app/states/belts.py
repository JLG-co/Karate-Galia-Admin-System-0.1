import reflex as rx
from ..models import BeltRank


class BeltState(rx.State):
    belts: list[BeltRank] = [
        BeltRank(
            name="White",
            color_hex="#FFFFFF",
            rank_order=1,
            description="Beginner level",
        ),
        BeltRank(
            name="Yellow",
            color_hex="#FACC15",
            rank_order=2,
            description="Basic fundamentals",
        ),
        BeltRank(
            name="Orange",
            color_hex="#F97316",
            rank_order=3,
            description="Intermediate skills",
        ),
        BeltRank(
            name="Green",
            color_hex="#22C55E",
            rank_order=4,
            description="Advanced techniques",
        ),
        BeltRank(
            name="Blue",
            color_hex="#3B82F6",
            rank_order=5,
            description="Proficiency level",
        ),
        BeltRank(
            name="Brown",
            color_hex="#78350F",
            rank_order=6,
            description="Expert preparation",
        ),
        BeltRank(
            name="Black", color_hex="#000000", rank_order=7, description="Mastery level"
        ),
    ]
    current_belt: BeltRank = BeltRank(name="", color_hex="#000000", rank_order=0)
    is_open: bool = False

    @rx.event
    def add_belt(self):
        """Add a new belt rank."""
        self.belts.append(self.current_belt)
        self.belts.sort(key=lambda b: b.rank_order)
        self.current_belt = BeltRank(name="", color_hex="#000000", rank_order=0)
        self.is_open = False
        return rx.toast.info("Belt rank added successfully")

    @rx.event
    def delete_belt(self, belt_idx: int):
        """Delete a belt rank."""
        self.belts.pop(belt_idx)
        return rx.toast.info("Belt rank deleted")

    @rx.event
    def set_current_belt_field(self, field: str, value: str):
        """Update a field in the current belt being edited."""
        setattr(self.current_belt, field, value)

    @rx.event
    def open_dialog(self):
        self.is_open = True

    @rx.event
    def close_dialog(self):
        self.is_open = False