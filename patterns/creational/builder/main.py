from patterns.creational.builder.builders.car_builder import CarBuilder
from patterns.creational.builder.builders.car_manual_builder import CarManualBuilder
from patterns.creational.builder.director.director import Director


def main() -> None:
    car_builder = CarBuilder()
    Director.construct_sports_car(car_builder)

    car = car_builder.get_product()

    manual_builder = CarManualBuilder()
    Director.construct_sports_car(manual_builder)

    manual = manual_builder.get_product()
    print(car)
    print(manual)


if __name__ == "__main__":
    main()
