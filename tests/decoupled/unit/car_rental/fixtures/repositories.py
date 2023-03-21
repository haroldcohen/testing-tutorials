from pytest import fixture

from decoupled.driven.repositories.in_memory.car_rental.repositories.command import CarRentalCommandInMemoryRepository
from decoupled.driven.repositories.in_memory.car_rental.repositories.query import CarRentalQueryRepository

__all__ = ["car_rental_query_repository", "car_rental_command_repository"]


@fixture
def car_rental_query_repository(unit_of_work):
    return CarRentalQueryRepository(
        unit_of_work=unit_of_work,
    )


@fixture
def car_rental_command_repository(unit_of_work):
    return CarRentalCommandInMemoryRepository(
        unit_of_work=unit_of_work,
    )
