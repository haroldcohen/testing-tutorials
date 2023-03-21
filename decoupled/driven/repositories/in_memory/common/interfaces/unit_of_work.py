"""unit_of_work"""
from abc import ABC, abstractmethod

from decoupled.driven.repositories.in_memory.common.entity import InMemoryEntity


class UnitOfWorkInterface(ABC):
    """UnitOfWorkInterface"""

    @abstractmethod
    def save_entity(self, entity: InMemoryEntity):
        """save_entity"""
