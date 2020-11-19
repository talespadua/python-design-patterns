from patterns.creational.factory.shipments.air_shipment import AirShipment
from patterns.creational.factory.shipments.land_shipment import LandShipment
from patterns.creational.factory.shipments.shipment import Shipment
from patterns.creational.factory.shipments.water_shipment import WaterShipment


class Application:
    shipment: Shipment

    def __init__(self, shipment_type: str):
        if shipment_type == "land":
            self.shipment = LandShipment()
        elif shipment_type == "air":
            self.shipment = AirShipment()
        elif shipment_type == "water":
            self.shipment = WaterShipment()
        else:
            raise NotImplementedError("Shipment Type Not Supported")

    def deliver(self) -> str:
        return self.shipment.transport_delivery()
