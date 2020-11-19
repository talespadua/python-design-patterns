from creational.factory.shipments.shipment import Shipment
from creational.factory.transport.ship import Ship


class WaterShipment(Shipment):
    def create_transport(self) -> Ship:
        return Ship()
