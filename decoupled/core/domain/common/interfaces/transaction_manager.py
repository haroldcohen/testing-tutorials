"""Provides with an interface for transaction managers"""
from abc import ABC, abstractmethod

from decoupled.core.domain.common.interfaces.transaction import TransactionInterface


class TransactionManagerInterface(ABC):
    @abstractmethod
    def new_transaction(self) -> TransactionInterface:
        pass
