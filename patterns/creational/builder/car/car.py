from typing import Optional


class Car:
    def __init__(self) -> None:
        self.seats: Optional[int] = None
        self.engine: Optional[str] = None
        self.trip_computer: Optional[bool] = None
        self.gps: Optional[str] = None

    def set_seats(self, seats: int) -> None:
        self.seats = seats

    def set_engine(self, engine: str) -> None:
        self.engine = engine

    def set_trip_computer(self) -> None:
        self.trip_computer = True

    def set_gps(self) -> None:
        self.gps = "gps"
