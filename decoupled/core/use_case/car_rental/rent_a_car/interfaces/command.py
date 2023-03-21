from abc import ABC, abstractmethod
import datetime
from typing import Dict
from uuid import UUID


class RentACarCommandInterface(ABC):
    @property
    @abstractmethod
    def car_id(self) -> UUID:
        """The UID of the car to be rented"""

    @property
    @abstractmethod
    def driver_information(self) -> Dict:
        """The name and driving license number of the driver"""

    @property
    @abstractmethod
    def rental_end_date(self) -> datetime.datetime:
        """The date at which the rental is supposed to end"""
