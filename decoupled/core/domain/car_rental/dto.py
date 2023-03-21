"""Provides with a DTO (Data Transfer Object) for the domain model 'CarRental'
"""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class CarRentalDTO:
    id: UUID
    car_id: UUID
