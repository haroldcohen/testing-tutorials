from uuid import UUID

from decoupled.core.domain.car_rental.dto import CarRentalDTO
from decoupled.core.domain.car_rental.interfaces.repositories.command import CarRentalCommandRepositoryInterface
from decoupled.core.domain.common.interfaces.transaction_manager import TransactionManagerInterface
from decoupled.core.use_case.car_rental.rent_a_car.interfaces.command import RentACarCommandInterface


class RentACar:
    def __init__(
        self,
        car_rental_command_repository: CarRentalCommandRepositoryInterface,
        transaction_manager: TransactionManagerInterface,
    ):
        self._car_rental_command_repository = car_rental_command_repository
        self._transaction_manager = transaction_manager

    def execute(self, command: RentACarCommandInterface) -> UUID:
        transaction = self._transaction_manager.new_transaction()
        car_rental_dto = CarRentalDTO(id=UUID("c044cc54-f9a7-4b8a-ac8d-01a9a0f3c702"), car_id=command.car_id)
        self._car_rental_command_repository.create(car_rental=car_rental_dto)
        transaction.commit()

        return UUID("c044cc54-f9a7-4b8a-ac8d-01a9a0f3c702")
