from patterns.creational.factory.transport.base_transport import BaseTransport


class Truck(BaseTransport):
    def deliver(self) -> str:
        return "delivery by truck"
