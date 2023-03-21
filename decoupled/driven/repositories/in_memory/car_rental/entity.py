from dataclasses import dataclass
import datetime
from uuid import UUID

from decoupled.driven.repositories.in_memory.common.entity import InMemoryEntity


@dataclass
class InMemoryCarRental(InMemoryEntity):
    class Config:
        storage_name = "car_rentals"

    id: UUID

    car_id: UUID

    end_date: datetime.datetime
