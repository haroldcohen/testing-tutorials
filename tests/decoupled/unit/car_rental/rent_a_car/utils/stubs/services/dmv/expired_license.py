from datetime import datetime, timedelta
from typing import Dict

from decoupled.core.domain.common.interfaces.services.dmv_interface import DMVServiceGatewayInterface


class DMVExpiredLicenseServiceStubGateway(DMVServiceGatewayInterface):
    def get_license_information(self, name: str, license_number: str) -> Dict:
        today = datetime.today()

        return {
            "delivery_date": datetime.strftime(today - timedelta(days=3650), "%Y-%m-%d"),
            "delivery_state": "Ohio",
            "valid_until": datetime.strftime(today - timedelta(days=1), "%Y-%m-%d"),
        }
