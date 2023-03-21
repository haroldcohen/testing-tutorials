from uuid import UUID, uuid4

from decoupled.core.domain.car_rental.interfaces.repositories.command import CarRentalCommandRepositoryInterface
from decoupled.core.domain.car_rental.model import CarRental
from decoupled.core.domain.common.interfaces.services.dmv_interface import DMVServiceGatewayInterface
from decoupled.core.domain.common.interfaces.transaction_manager import TransactionManagerInterface
from decoupled.core.use_case.car_rental.rent_a_car.interfaces.command import RentACarCommandInterface


class RentACar:
    def __init__(
        self,
        car_rental_command_repository: CarRentalCommandRepositoryInterface,
        transaction_manager: TransactionManagerInterface,
        dmv_service_gateway: DMVServiceGatewayInterface,
    ):
        self._car_rental_command_repository = car_rental_command_repository
        self._transaction_manager = transaction_manager
        self._dmv_service_gateway = dmv_service_gateway

    def execute(self, command: RentACarCommandInterface) -> UUID:
        transaction = self._transaction_manager.new_transaction()
        car_rental = CarRental(
            _id=uuid4(),
            car_id=command.car_id,
            end_date=command.rental_end_date,
        )
        car_rental.driver_may_rent_car(
            driver_information=command.driver_information, dmv_service_gateway=self._dmv_service_gateway
        )
        car_rental_dto = car_rental.to_dto()
        self._car_rental_command_repository.create(car_rental=car_rental_dto)
        transaction.commit()

        return car_rental_dto.id
