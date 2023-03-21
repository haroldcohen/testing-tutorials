"""manager"""
from decoupled.core.domain.common.interfaces.transaction_manager import TransactionManagerInterface
from decoupled.driven.repositories.in_memory.common.interfaces.unit_of_work_originator import (
    UnitOfWorkOriginatorInterface,
)
from decoupled.driven.repositories.in_memory.common.transaction import InMemoryTransaction


class InMemoryTransactionManager(TransactionManagerInterface):
    """InMemoryTransactionManager"""

    def __init__(self, unit_of_work: UnitOfWorkOriginatorInterface):
        self._unit_of_work = unit_of_work

    def new_transaction(self) -> InMemoryTransaction:
        """new_transaction"""
        return InMemoryTransaction(originator=self._unit_of_work)
