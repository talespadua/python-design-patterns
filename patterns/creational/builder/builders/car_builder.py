from patterns.creational.builder.builders.abc_builder import AbstractBuilder
from patterns.creational.builder.car.car import Car


class CarBuilder(AbstractBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def set_seats(self, seats: int) -> None:
        self._car.set_seats(seats)

    def set_engine(self, engine: str) -> None:
        self._car.set_engine(engine)

    def set_trip_computer(self) -> None:
        self._car.set_trip_computer()

    def set_gps(self) -> None:
        self._car.set_gps()

    def get_product(self) -> Car:
        product = self._car
        self.reset()
        return product
