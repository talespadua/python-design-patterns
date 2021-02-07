from patterns.structural.adapter.shapes.roud_peg import RoundPeg
from patterns.structural.adapter.shapes.square_peg import SquarePeg
from math import sqrt


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        self._peg = peg

    def get_radius(self) -> int:
        return int(self._peg.get_width() * sqrt(2) / 2)
