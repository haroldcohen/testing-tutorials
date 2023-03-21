from dataclasses import dataclass
import datetime
from typing import Dict
from uuid import UUID

from decoupled.core.use_case.car_rental.rent_a_car.interfaces.command import RentACarCommandInterface


@dataclass
class RentACarCommand(RentACarCommandInterface):
    __slots__ = ["car_id", "driver_information", "rental_end_date"]

    car_id: UUID

    driver_information: Dict

    rental_end_date: datetime.datetime
