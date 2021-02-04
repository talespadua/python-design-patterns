from typing import List, Dict, Any

import pytest

from patterns.creational.builder.builders.car_builder import CarBuilder
from patterns.creational.builder.car.car import Car


class TestCarBuilder:
    @pytest.fixture()
    def car_builder(self) -> CarBuilder:
        return CarBuilder()

    @pytest.fixture()
    def cars_parameters(self) -> List[Dict[str, Any]]:
        return [
            {
                "seats": 2,
                "engine": "turbo",
                "trip_computer": True,
                "gps": False,
            },
        ]

    @pytest.fixture()
    def car(self, car_builder: CarBuilder, car_parameters: Dict[str, Any]) -> Car:
        car_builder.reset()
        car_builder.set_seats(car_parameters["seats"])
        car_builder.set_engine(car_parameters["engine"])
        if car_parameters["trip_computer"]:
            car_builder.set_trip_computer()
        if car_parameters["gps"]:
            car_builder.set_gps()

        return car_builder.get_product()

    @pytest.mark.parametrize(
        "car_parameters",
        [
            (
                {
                    "seats": 2,
                    "engine": "turbo",
                    "trip_computer": True,
                    "gps": False,
                }
            ),
            (
                {
                    "seats": 4,
                    "engine": "economic",
                    "trip_computer": False,
                    "gps": True,
                }
            ),
        ],
    )
    def test_car_builder(self, car_parameters: Dict[str, Any], car: Car) -> None:
        assert car.seats == car_parameters["seats"]
        assert car.engine == car_parameters["engine"]
        assert car.trip_computer == car_parameters["trip_computer"]
        assert car.gps == car_parameters["gps"]
