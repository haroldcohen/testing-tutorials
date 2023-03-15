"""This file provides with a gateway to query the DMV service."""
from typing import Dict
import urllib.parse

import requests

from decoupled.core.use_case.common.services.dmv_interface import DMVServiceGatewayInterface


class DMVServiceGateway(DMVServiceGatewayInterface):  # pylint: disable=too-few-public-methods
    """Allows to query the DMV"""

    def __init__(self, gateway_url: str):
        self._gateway_url = gateway_url

    def get_license_information(self, name: str, license_number: str) -> Dict:
        """Returns information on a driver's license."""
        return requests.get(  # pylint: disable=missing-timeout
            f"{self._gateway_url}/license-information?"
            + urllib.parse.urlencode({"name": name, "licenceNumber": license_number}),
        ).json()
