from abc import ABC, abstractmethod
from creational.factory.transport.base_transport import BaseTransport


# This is the base creator class
class Shipment(ABC):
    # This is the base factory method, that should be overridden to create the concrete
    # transport type
    @abstractmethod
    def create_transport(self) -> BaseTransport:
        ...

    # Base business logic for all the shipments
    def transport_delivery(self) -> str:
        transport = self.create_transport()
        return transport.deliver()
