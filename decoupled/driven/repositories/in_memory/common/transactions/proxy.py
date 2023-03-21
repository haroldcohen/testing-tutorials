"""Provides with a Proxy to implement TransactionManagerInterface"""
from decoupled.core.domain.common.interfaces.transaction_manager import TransactionManagerInterface
from decoupled.driven.repositories.in_memory.common.interfaces.unit_of_work_originator import (
    UnitOfWorkOriginatorInterface,
)
from decoupled.driven.repositories.in_memory.common.transaction import InMemoryTransaction
from decoupled.driven.repositories.in_memory.common.transactions import InMemoryTransactionManager


class InMemoryTransactionManagerProxy(TransactionManagerInterface):
    def __init__(self, unit_of_work: UnitOfWorkOriginatorInterface):
        self._transaction_manager = InMemoryTransactionManager(unit_of_work=unit_of_work)

    def new_transaction(self) -> InMemoryTransaction:
        """new_transaction"""
        return self._transaction_manager.new_transaction()
