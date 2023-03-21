"""This file provides with an example of unit test for a use case where the persona wants to
rent a car.

The example below applies to decoupled architectures, where IOC (Inversion Of Control) is made possible.
"""
from datetime import datetime, timedelta
from typing import Dict
from uuid import UUID, uuid4

from hamcrest import assert_that, calling, equal_to, raises
import pytest

from decoupled.core.domain.car_rental.dto import CarRentalDTO
from decoupled.core.domain.car_rental.exceptions.expired_license import CannotRentACarWithExpiredLicense
from decoupled.core.use_case.car_rental.rent_a_car.handler import RentACar
from tests.decoupled.unit.car_rental.fixtures.repositories import *
from tests.decoupled.unit.car_rental.fixtures.services import *
from tests.decoupled.unit.car_rental.rent_a_car.utils.command_bus.command import RentACarCommand
from tests.decoupled.unit.fixtures.repositories import *


@pytest.mark.parametrize(
    "car_id, driver, rental_end_date",
    [
        (uuid4(), {"name": "Obi-Wan Kenobi", "license_number": "ALD-726-616-984"}, datetime.now() + timedelta(days=10)),
        (uuid4(), {"name": "Bo Katan", "license_number": "MAN-726-444-984"}, datetime.now() + timedelta(days=20)),
    ],
)
def test_rent_a_car_should_create_a_new_car_rental(
    car_rental_query_repository,
    car_rental_command_repository,
    in_memory_transaction_manager,
    car_id: UUID,
    driver: Dict,
    dmv_stub_service_gateway,
    rental_end_date,
):
    uc: RentACar = RentACar(
        car_rental_command_repository=car_rental_command_repository,
        transaction_manager=in_memory_transaction_manager,
        dmv_service_gateway=dmv_stub_service_gateway,
    )
    # Depending on your implementation of CQRS, your use might return just an ID or a complete data structure.
    car_rental_id = uc.execute(
        command=RentACarCommand(
            car_id=car_id,
            driver_information=driver,
            rental_end_date=rental_end_date,
        )
    )
    expected_car_rental = CarRentalDTO(
        id=car_rental_id,
        car_id=car_id,
        end_date=rental_end_date,
    )
    retrieved_car_rental = car_rental_query_repository.read(car_rental_id=car_rental_id).to_dto()
    assert_that(retrieved_car_rental, equal_to(expected_car_rental))


@pytest.mark.parametrize(
    "car_id, driver, rental_end_date",
    [
        (uuid4(), {"name": "Din Djarin", "license_number": "MAN-726-616-984"}, datetime.now() + timedelta(days=10)),
    ],
)
def test_rent_a_car_should_raise_CannotRentACarWithExpiredLicense(
    car_rental_command_repository,
    in_memory_transaction_manager,
    dmv_expired_license_stub_service_gateway,
    car_id: UUID,
    driver: Dict,
    rental_end_date: datetime,
):
    uc: RentACar = RentACar(
        car_rental_command_repository=car_rental_command_repository,
        transaction_manager=in_memory_transaction_manager,
        dmv_service_gateway=dmv_expired_license_stub_service_gateway,
    )
    assert_that(
        calling(uc.execute).with_args(
            command=RentACarCommand(
                car_id=car_id,
                driver_information=driver,
                rental_end_date=rental_end_date,
            )
        ),
        raises(CannotRentACarWithExpiredLicense),
    )
