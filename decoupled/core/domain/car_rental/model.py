from uuid import UUID

from decoupled.core.domain.car_rental.dto import CarRentalDTO


class CarRental:
    def __init__(self, _id: UUID, car_id: UUID):
        self._id = _id
        self._car_id = car_id

    def to_dto(self) -> CarRentalDTO:
        return CarRentalDTO(
            id=self._id,
            car_id=self._car_id,
        )
