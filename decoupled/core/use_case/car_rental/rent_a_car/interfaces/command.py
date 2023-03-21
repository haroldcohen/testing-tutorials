from abc import ABC, abstractmethod
from uuid import UUID


class RentACarCommandInterface(ABC):
    @property
    @abstractmethod
    def car_id(self) -> UUID:
        """The UID of the car to be rented"""
