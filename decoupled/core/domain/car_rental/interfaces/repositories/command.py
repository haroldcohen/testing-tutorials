from abc import ABC, abstractmethod

from decoupled.core.domain.car_rental.dto import CarRentalDTO


class CarRentalCommandRepositoryInterface(ABC):
    @abstractmethod
    def create(self, car_rental: CarRentalDTO):
        """Creates and store a car rental"""
