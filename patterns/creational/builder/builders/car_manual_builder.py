from patterns.creational.builder.builders.abc_builder import AbstractBuilder
from patterns.creational.builder.manual.car_manual import CarManual


class CarManualBuilder(AbstractBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._manual = CarManual()

    def set_seats(self, seats: int) -> None:
        self._manual.set_seats(seats)

    def set_engine(self, engine: str) -> None:
        self._manual.set_engine(engine)

    def set_trip_computer(self) -> None:
        self._manual.set_trip_computer()

    def set_gps(self) -> None:
        self._manual.set_gps()

    def get_product(self) -> CarManual:
        product = self._manual
        self.reset()
        return product
