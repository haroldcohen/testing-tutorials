"""This file provides with fixtures related to contract/consumer driven testing."""
import atexit

from pact import Consumer, Pact, Provider
from pytest import fixture

__all__ = ["pact_broker"]

PACT_BROKERS_REGISTRY = {1234: {"state": 0, "broker": Consumer("Our service").has_pact_with(Provider("DMV"))}}


@fixture
def pact_broker() -> Pact:
    """Provides with a Pact broker to run with consumer driven tests."""
    broker = PACT_BROKERS_REGISTRY[1234]["broker"]
    if not PACT_BROKERS_REGISTRY[1234]["state"]:
        broker.start_service()
        atexit.register(broker.stop_service)

    return PACT_BROKERS_REGISTRY[1234]["broker"]
