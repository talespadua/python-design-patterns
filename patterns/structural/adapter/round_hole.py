from patterns.structural.adapter.shapes.roud_peg import RoundPeg


class RoundHole:
    def __init__(self, radius: int) -> None:
        self._radius = radius

    def get_radius(self) -> int:
        return self._radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.get_radius() >= peg.get_radius()
