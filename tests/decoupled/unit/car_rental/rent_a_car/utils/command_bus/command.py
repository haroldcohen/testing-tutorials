from dataclasses import dataclass
from uuid import UUID

from decoupled.core.use_case.car_rental.rent_a_car.interfaces.command import RentACarCommandInterface


@dataclass
class RentACarCommand(RentACarCommandInterface):
    __slots__ = ["car_id"]

    car_id: UUID
