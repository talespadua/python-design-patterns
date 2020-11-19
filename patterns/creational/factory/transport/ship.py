from patterns.creational.factory.transport.base_transport import BaseTransport


class Ship(BaseTransport):
    def deliver(self) -> str:
        return "delivery by ship"
