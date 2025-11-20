import reflex as rx
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class User(BaseModel):
    """User model for authentication and role management."""

    username: str
    password_hash: str
    role: str
    email: str
    full_name: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True


class BeltRank(BaseModel):
    """Belt rank definitions (e.g., White, Yellow, Black)."""

    name: str
    color_hex: str
    rank_order: int
    description: str = ""


class Athlete(BaseModel):
    """Athlete/Student profile information."""

    first_name: str
    last_name: str
    email: str = ""
    phone: str = ""
    birth_date: datetime = Field(default_factory=datetime.now)
    gender: str = ""
    belt_rank_id: int = 0
    join_date: datetime = Field(default_factory=datetime.now)
    is_active: bool = True
    parent_name: str = ""
    parent_phone: str = ""
    address: str = ""
    notes: str = ""


class Coach(BaseModel):
    """Coach profile information."""

    user_id: int = 0
    first_name: str
    last_name: str
    specialty: str = ""
    bio: str = ""
    phone: str = ""


class Payment(BaseModel):
    """Financial records."""

    athlete_id: int
    amount: float
    payment_date: datetime = Field(default_factory=datetime.now)
    payment_type: str
    status: str = "completed"
    notes: str = ""


class Attendance(BaseModel):
    """Daily attendance records."""

    athlete_id: int
    date: datetime = Field(default_factory=datetime.now)
    status: str
    notes: str = ""
    class_type: str = "general"


class Competition(BaseModel):
    """Competition event details."""

    name: str
    date: datetime
    location: str
    description: str = ""
    registration_deadline: datetime = Field(default_factory=datetime.now)
    fee: float = 0.0