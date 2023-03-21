from uuid import UUID

from decoupled.core.domain.car_rental.model import CarRental
from decoupled.driven.repositories.in_memory.car_rental.entity import InMemoryCarRental
from decoupled.driven.repositories.in_memory.common.unit_of_work import UnitOfWork


class CarRentalQueryRepository:
    def __init__(self, unit_of_work: UnitOfWork):
        self.unit_of_work = unit_of_work

    def read(self, car_rental_id: UUID):
        filtered: InMemoryCarRental = self.unit_of_work.car_rentals[car_rental_id]
        return CarRental(
            _id=filtered.id,
            car_id=filtered.car_id,
            end_date=filtered.end_date,
        )
