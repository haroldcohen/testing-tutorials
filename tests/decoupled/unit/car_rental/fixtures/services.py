from pytest import fixture

from tests.decoupled.unit.car_rental.rent_a_car.utils.stubs.services.dmv.base import DMVServiceStubGateway
from tests.decoupled.unit.car_rental.rent_a_car.utils.stubs.services.dmv.expired_license import (
    DMVExpiredLicenseServiceStubGateway,
)

__all__ = ["dmv_stub_service_gateway", "dmv_expired_license_stub_service_gateway"]


@fixture
def dmv_stub_service_gateway(rental_end_date):
    return DMVServiceStubGateway(rental_end_date=rental_end_date)


@fixture
def dmv_expired_license_stub_service_gateway():
    return DMVExpiredLicenseServiceStubGateway()
