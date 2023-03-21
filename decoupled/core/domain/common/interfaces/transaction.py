"""Provides with an interface for transactions"""
from abc import ABC, abstractmethod


class TransactionInterface(ABC):
    @abstractmethod
    def commit(self):
        pass
