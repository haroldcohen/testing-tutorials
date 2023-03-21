"""Provides with repositories fixtures
Obviously, in a real project it would be preferable to use an injection dependence library to avoid the fixtures below.
"""
import time

from pytest import fixture

from decoupled.driven.repositories.in_memory.common.transactions import InMemoryTransactionManager
from decoupled.driven.repositories.in_memory.common.unit_of_work import UnitOfWork

__all__ = ["unit_of_work", "in_memory_transaction_manager"]


@fixture
def unit_of_work() -> UnitOfWork:  # pylint: disable=redefined-outer-name
    return UnitOfWork(state=time.time_ns())


@fixture
def in_memory_transaction_manager(unit_of_work) -> InMemoryTransactionManager:  # pylint: disable=redefined-outer-name
    return InMemoryTransactionManager(unit_of_work=unit_of_work)
