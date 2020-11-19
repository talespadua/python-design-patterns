import pytest

from patterns.creational.factory.application import Application


class TestApplicationTransportDelivery:
    class TestGivenValidShipmentType:
        @pytest.fixture()
        def delivery(self, shipment_type: str) -> str:
            application = Application(shipment_type)
            return application.deliver()

        @pytest.mark.parametrize(
            "shipment_type, expected_delivery",
            [
                ("land", "delivery by truck"),
                ("air", "delivery by airplane"),
                ("water", "delivery by ship"),
            ],
        )
        def test_delivery_should_match_shipment_type(
            self, shipment_type: str, expected_delivery: str, delivery: str
        ) -> None:
            assert expected_delivery == delivery

    class TestGivenInvalidShipmentType:
        def test_should_raise_not_implemented_error(self) -> None:
            with pytest.raises(NotImplementedError):
                application = Application("invalid shipment")
                application.deliver()
