"""Provides with an interface for services capable of querying the DMV."""
from abc import ABC, abstractmethod


class DMVServiceGatewayInterface(ABC):  # pylint: disable=too-few-public-methods
    """DMVServiceGatewayInterface"""

    @abstractmethod
    def get_license_information(self, name: str, license_number: str):
        """get_license_information"""
