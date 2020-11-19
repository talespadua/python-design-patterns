from patterns.creational.factory.transport.base_transport import BaseTransport


class Airplane(BaseTransport):
    def deliver(self) -> str:
        return "delivery by airplane"
