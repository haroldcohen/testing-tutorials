"""unit_of_work_originator"""
from abc import ABC, abstractmethod

from decoupled.driven.repositories.in_memory.common.unit_of_work_memento import UnitOfWorkMemento


class UnitOfWorkOriginatorInterface(ABC):
    """UnitOfWorkOriginatorInterface"""

    @abstractmethod
    def save(self) -> UnitOfWorkMemento:
        """save"""

    @abstractmethod
    def restore(self, memento: UnitOfWorkMemento):
        """restore"""
