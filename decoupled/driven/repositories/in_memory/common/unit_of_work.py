"""unit_of_work"""
from copy import deepcopy
import time

from decoupled.driven.repositories.in_memory.common.entity import InMemoryEntity
from decoupled.driven.repositories.in_memory.common.interfaces.unit_of_work import UnitOfWorkInterface
from decoupled.driven.repositories.in_memory.common.interfaces.unit_of_work_originator import (
    UnitOfWorkOriginatorInterface,
)
from decoupled.driven.repositories.in_memory.common.unit_of_work_memento import UnitOfWorkMemento

__all__ = ["UnitOfWork"]


class UnitOfWork(UnitOfWorkInterface, UnitOfWorkOriginatorInterface):
    """UnitOfWork"""

    __slots__ = ["profiles", "actions"]

    def __init__(
        self,
        state: int,
    ):
        self.state = state
        self.car_rentals = {}
        self.replica = {"state": state, "car_rentals": deepcopy(self.car_rentals)}

    def save(self) -> UnitOfWorkMemento:
        """save"""
        self.state = deepcopy(self.replica["state"])
        self.car_rentals = deepcopy(self.replica["car_rentals"])
        return UnitOfWorkMemento(
            state=self.state,
        )

    def save_entity(self, entity: InMemoryEntity):
        """save_entity"""
        self.replica["state"] = time.time_ns()
        self.replica[entity.Config.storage_name][entity.id] = entity

    def restore(self, memento: UnitOfWorkMemento):
        """restore"""
        self.replica["state"] = memento.state

    def reset(self, state: int):
        self.state = state
        self.replica = {
            "state": state,
        }

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            attributes_to_compare = list(
                filter(
                    lambda a: not a.startswith("_") and a not in ["save_entity", "save", "restore", "replica"],
                    dir(self),
                )
            )
            for attribute in attributes_to_compare:
                if getattr(self, attribute) != getattr(other, attribute):
                    return False
            return True
        return False
