from patterns.creational.builder.builders.abc_builder import AbstractBuilder


class Director:
    @staticmethod
    def construct_sports_car(builder: AbstractBuilder) -> None:
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("sports engine")
        builder.set_trip_computer()
        builder.set_gps()

    @staticmethod
    def construct_suv(builder: AbstractBuilder) -> None:
        builder.reset()
        builder.set_seats(4)
        builder.set_engine("SUV engine")
        builder.set_trip_computer()
        builder.set_gps()
