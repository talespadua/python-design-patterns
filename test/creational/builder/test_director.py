from typing import Any

import pytest

from patterns.creational.builder.builders.car_builder import CarBuilder
from patterns.creational.builder.builders.car_manual_builder import CarManualBuilder
from patterns.creational.builder.car.car import Car
from patterns.creational.builder.director import Director
from patterns.creational.builder.manual.car_manual import CarManual


class TestDirector:
    @pytest.fixture()
    def director(self) -> Director:
        return Director()

    @pytest.fixture()
    def car_builder(self) -> CarBuilder:
        return CarBuilder()

    @pytest.fixture()
    def car_manual_builder(self) -> CarManualBuilder:
        return CarManualBuilder()

    @pytest.mark.parametrize(
        "builder, expected_type",
        [
            (CarBuilder(), Car),
            (CarManualBuilder(), CarManual),
        ],
    )
    def test_build_suv_director(
        self, builder: Any, expected_type: Any, director: Director
    ) -> None:
        director.construct_suv(builder)
        assert isinstance(builder.get_product(), expected_type)

        builder.reset()

        director.construct_sports_car(builder)
        assert isinstance(builder.get_product(), expected_type)
