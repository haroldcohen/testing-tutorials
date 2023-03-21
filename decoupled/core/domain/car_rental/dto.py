"""Provides with a DTO (Data Transfer Object) for the domain model 'CarRental'
"""
from dataclasses import dataclass
import datetime
from uuid import UUID


@dataclass
class CarRentalDTO:
    id: UUID

    car_id: UUID

    end_date: datetime.datetime
