from patterns.creational.factory.shipments.shipment import Shipment
from patterns.creational.factory.transport.truck import Truck


class LandShipment(Shipment):
    def create_transport(self) -> Truck:
        return Truck()
