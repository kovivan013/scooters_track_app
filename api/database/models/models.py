from typing import Optional, Union
from .base import Base
from sqlalchemy import (
    Integer,
    BigInteger,
    JSON,
    Numeric,
    String,
    SmallInteger,
    Boolean,
    ARRAY,
    UUID
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped
)
from schemas.schemas import (
    BaseUser,
    BaseAdmin,
    BannedUser,
    BaseScooter,
    BaseNews,
    BaseTrip,
    UserNotifications
)


class Users(Base):

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        index=True,
        primary_key=True
    )
    firstname: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    lastname: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    phone_number: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    email: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    rides: Mapped[Integer] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )
    passed: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False,
        default=0
    )
    created_at: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    balance: Mapped[Numeric] = mapped_column(
        Numeric,
        nullable=False,
        default=0
    )

    def as_model(self) -> Union[BaseUser]:
        return BaseUser().model_validate(
            self.as_dict()
        )


class Admins(Base):

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        index=True,
        primary_key=True
    )
    administrator: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    rank: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        default=1
    )
    permissions: Mapped[JSON] = mapped_column(
        JSON,
        nullable=False,
        default={}
    )
    added_at: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )

    def as_model(self) -> Union[BaseAdmin]:
        return BaseAdmin().model_validate(
            self.as_dict()
        )


class BannedUsers(Base):

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True
    )
    administrator: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    reason: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    banned_at: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    until: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False,
        default=0
    )

    def as_model(self) -> Union[BannedUser]:
        return BannedUser().model_validate(
            self.as_dict()
        )


class Notifications(Base):

    user_id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True
    )
    details: Mapped[JSON] = mapped_column(
        JSON,
        nullable=False,
        default={}
    )
    content: Mapped[JSON] = mapped_column(
        JSON,
        nullable=False,
        default={}
    )

    def as_model(self) -> Union[UserNotifications]:
        return UserNotifications().model_validate(
            self.as_dict()
        )


class Scooters(Base):

    id: Mapped[Integer] = mapped_column(
        Integer,
        index=True,
        primary_key=True
    )
    alias: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    available: Mapped[Boolean] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )
    charge: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        default=0
    )
    location: Mapped[JSON] = mapped_column(
        JSON,
        nullable=False,
        default={}
    )

    def as_model(self) -> Union[BaseScooter]:
        return BaseScooter().model_validate(
            self.as_dict()
        )


class Trips(Base):

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True
    )
    user_id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    scooter_id: Mapped[Integer] = mapped_column(
        Integer,
        nullable=False
    )
    start_time: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    end_time: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    distance: Mapped[Numeric] = mapped_column(
        Numeric,
        nullable=False,
        default=0
    )
    price: Mapped[Numeric] = mapped_column(
        Numeric,
        nullable=False,
        default=0
    )
    path: Mapped[ARRAY] = mapped_column(
        ARRAY(Numeric),
        nullable=False,
        default=[]
    )

    def as_model(self) -> Union[BaseTrip]:
        return BaseTrip().model_validate(
            self.as_dict()
        )


class News(Base):

    id: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        index=True
    )
    administrator: Mapped[BigInteger] = mapped_column(
        BigInteger,
        nullable=False
    )
    content: Mapped[String] = mapped_column(
        String,
        nullable=False
    )
    image: Mapped[String] = mapped_column(
        String,
        nullable=False
    )

    def as_model(self) -> Union[BaseNews]:
        return BaseNews().model_validate(
            self.as_dict()
        )




