import pytest

from patterns.structural.adapter.round_hole import RoundHole
from patterns.structural.adapter.shapes.roud_peg import RoundPeg
from patterns.structural.adapter.shapes.square_peg import SquarePeg
from patterns.structural.adapter.shapes.square_peg_adapter import SquarePegAdapter


class TestSquarePegAdapter:
    @pytest.fixture()
    def round_hole(self) -> RoundHole:
        return RoundHole(5)

    @pytest.fixture()
    def round_peg(self) -> RoundPeg:
        return RoundPeg(5)

    @pytest.fixture()
    def small_square_peg(self) -> SquarePeg:
        return SquarePeg(3)

    @pytest.fixture()
    def small_square_adapter(self, small_square_peg: SquarePeg) -> SquarePegAdapter:
        return SquarePegAdapter(small_square_peg)

    @pytest.fixture()
    def big_square_adapter(self, big_square_peg: SquarePeg) -> SquarePegAdapter:
        return SquarePegAdapter(big_square_peg)

    @pytest.fixture()
    def big_square_peg(self) -> SquarePeg:
        return SquarePeg(10)

    def test_square_peg_adapter(
        self,
        round_peg: RoundPeg,
        round_hole: RoundHole,
        small_square_adapter: SquarePegAdapter,
        big_square_adapter: SquarePegAdapter,
    ) -> None:
        assert round_hole.fits(round_peg)
        assert round_hole.fits(small_square_adapter)
        assert not round_hole.fits(big_square_adapter)
