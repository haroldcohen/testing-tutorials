import datetime
from typing import Dict
from uuid import UUID

from decoupled.core.domain.car_rental.dto import CarRentalDTO
from decoupled.core.domain.car_rental.exceptions.expired_license import CannotRentACarWithExpiredLicense
from decoupled.core.domain.common.interfaces.services.dmv_interface import DMVServiceGatewayInterface


class CarRental:
    def __init__(self, _id: UUID, car_id: UUID, end_date: datetime.datetime):
        self._id = _id
        self._car_id = car_id
        self._end_date = end_date

    def driver_may_rent_car(
        self,
        driver_information: Dict,
        dmv_service_gateway: DMVServiceGatewayInterface,
    ):
        driver_licence_information = dmv_service_gateway.get_license_information(
            name=driver_information["name"],
            license_number=driver_information["license_number"],
        )
        driver_license_expiration_date = datetime.datetime.strptime(
            driver_licence_information["valid_until"], "%Y-%m-%d"
        )
        if self._end_date > driver_license_expiration_date:
            raise CannotRentACarWithExpiredLicense

    def to_dto(self) -> CarRentalDTO:
        return CarRentalDTO(
            id=self._id,
            car_id=self._car_id,
            end_date=self._end_date,
        )
