from typing import Union, Dict, List, Any
from pydantic import BaseModel


class BaseUser(BaseModel):

    id: int = 0
    firstname: str = ""
    lastname: str = ""
    phone_number: str = ""
    email: str = ""
    rides: int = 0
    passed: int = 0
    created_at: int = 0
    balance: float = 0



class BaseAdmin(BaseModel):

    id: int = 0
    administrator: int = 0
    rank: int = 1
    permissions: Dict[str, bool] = {}
    added_at: int = 0


class ScooterLocation(BaseModel):

    latitude: float = 0
    longitude: float = 0


class BaseScooter(BaseModel):

    id: int = 0
    alias: str = ""
    available: bool = False
    charge: int = 0
    location: ScooterLocation = ScooterLocation()


class BannedUser(BaseModel):

    id: int = 0
    administrator: int = 0
    reason: str = 0
    banned_at: int = 0
    until: int = 0


class BaseNotification(BaseModel):
    pass


class UserNotifications(BaseModel):

    user_id: int = 0
    details: Dict[str, Any] = {}
    content: Dict[str, Any] = {}


class BaseTrip(BaseModel):

    id: int = 0
    user_id: int = 0
    scooter_id: int = 0
    start_time: int = 0
    end_time: int = 0
    distance: float = 0
    price: float = 0
    path: List[float] = []


class BaseNews(BaseModel):

    id: str = ""
    administrator: int = 0
    content: str = ""
    image: str = ""