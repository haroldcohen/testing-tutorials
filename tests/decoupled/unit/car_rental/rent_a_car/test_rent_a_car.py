"""This file provides with an example of unit test for a use case where the persona wants to
rent a car.

The example below applies to decoupled architectures, where IOC (Inversion Of Control) is made possible.
"""
from uuid import UUID, uuid4

from hamcrest import assert_that, equal_to
import pytest

from decoupled.core.domain.car_rental.dto import CarRentalDTO
from decoupled.core.use_case.car_rental.rent_a_car.handler import RentACar
from tests.decoupled.unit.car_rental.fixtures.repositories import *
from tests.decoupled.unit.car_rental.rent_a_car.utils.command_bus.command import RentACarCommand
from tests.decoupled.unit.fixtures.repositories import *


@pytest.mark.parametrize(
    "car_id",
    [
        UUID("62b4062c-d1b6-4dcc-8c78-dc453ea36995"),
        uuid4(),
    ],
)
def test_rent_a_car_should_create_a_new_car_rental(
    car_rental_query_repository,
    car_rental_command_repository,
    in_memory_transaction_manager,
    car_id: UUID,
):
    uc: RentACar = RentACar(
        car_rental_command_repository=car_rental_command_repository,
        transaction_manager=in_memory_transaction_manager,
    )
    # Depending on your implementation of CQRS, your use might return just an ID or a complete data structure.
    car_rental_id = uc.execute(command=RentACarCommand(car_id=car_id))
    expected_car_rental = CarRentalDTO(
        id=car_rental_id,
        car_id=car_id,
    )
    retrieved_car_rental = car_rental_query_repository.read(car_rental_id=car_rental_id).to_dto()
    assert_that(retrieved_car_rental, equal_to(expected_car_rental))
