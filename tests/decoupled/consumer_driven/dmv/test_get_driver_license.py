"""
This file provides with an example of contract tests
for some service called DMV that would provide with information on a driver license.

Also known as consumer driven tests, contract testing aims to validate that your software
is capable of communicating
with a Producer.
"""
import urllib.parse

from hamcrest import assert_that, equal_to
import pytest

from decoupled.driven.services.dmv import DMVServiceGateway
from tests.decoupled.consumer_driven.fixtures import pact_broker  # pylint: disable=unused-import


@pytest.mark.parametrize(
    "driver, license_number, expected_response",
    [
        (
            "Bo Katan",
            "S-514-726-616-984",
            {
                "delivery_date": "2021-01-01",
                "delivery_state": "Massachusetts",
                "valid_until": "2031-01-01",
            },
        ),
        (
            "Din Djarin",
            "L-512-726-878-458",
            {
                "delivery_date": "2020-05-01",
                "delivery_state": "Ohio",
                "valid_until": "2030-05-01",
            },
        ),
    ],
)
def test_get_driver_license_should_return_a_drivers_license(
    pact_broker,  # pylint: disable=redefined-outer-name
    driver,
    license_number,
    expected_response,
):
    """Tests whether our service is capable of querying and handling the DMV service for license information."""
    query = urllib.parse.urlencode(
        {
            "name": driver,
            "licenceNumber": license_number,
        }
    )
    (
        pact_broker.given(f"Driver {driver} has a driving license {license_number}")
        .upon_receiving("a request to get the driver's information")
        .with_request(
            "get",
            "/api/license-information",
            query=query,
        )
        .will_respond_with(200, body=expected_response)
    )
    gateway = DMVServiceGateway(gateway_url="http://localhost:1234/api")
    pact_broker.setup()
    response = gateway.get_license_information(
        name=driver,
        license_number=license_number,
    )
    assert_that(response, equal_to(expected_response))
    pact_broker.verify()
