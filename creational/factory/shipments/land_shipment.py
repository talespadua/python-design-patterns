from creational.factory.shipments.shipment import Shipment
from creational.factory.transport.truck import Truck


class LandShipment(Shipment):
    def create_transport(self) -> Truck:
        return Truck()
