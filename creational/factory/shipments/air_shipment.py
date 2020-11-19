from creational.factory.shipments.shipment import Shipment
from creational.factory.transport.airplane import Airplane


class AirShipment(Shipment):
    def create_transport(self) -> Airplane:
        return Airplane()
