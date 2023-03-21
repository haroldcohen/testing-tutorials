from decoupled.core.domain.car_rental.dto import CarRentalDTO
from decoupled.core.domain.car_rental.interfaces.repositories.command import CarRentalCommandRepositoryInterface
from decoupled.driven.repositories.in_memory.car_rental.entity import InMemoryCarRental
from decoupled.driven.repositories.in_memory.common.unit_of_work import UnitOfWork


class CarRentalCommandInMemoryRepository(CarRentalCommandRepositoryInterface):
    def __init__(self, unit_of_work: UnitOfWork):
        self._unit_of_work = unit_of_work

    def create(self, car_rental: CarRentalDTO):
        self._unit_of_work.save_entity(
            entity=InMemoryCarRental(
                id=car_rental.id,
                car_id=car_rental.car_id,
                end_date=car_rental.end_date,
            )
        )
