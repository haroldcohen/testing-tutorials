from typing import Generator, List

from decoupled.driven.repositories.in_memory.common.interfaces.unit_of_work_originator import (
    UnitOfWorkOriginatorInterface,
)
from decoupled.driven.repositories.in_memory.common.unit_of_work_memento import UnitOfWorkMemento


class InMemoryTransaction:
    """InMemoryTransaction"""

    def __init__(self, originator: UnitOfWorkOriginatorInterface):
        self.originator = originator
        self._mementos: List[UnitOfWorkMemento] = []
        self._mementos.append(self.originator.save())

    def commit(self):
        """commit"""
        self._mementos.append(self.originator.save())

    def rollback(self):
        """rollback"""
        memento = self._mementos.pop()
        self.originator.restore(memento=memento)

    def history(self) -> Generator[UnitOfWorkMemento, None, None]:
        """history"""
        for memento in self._mementos:
            yield memento
