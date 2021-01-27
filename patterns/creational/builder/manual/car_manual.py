from typing import Optional


class CarManual:
    def __init__(self) -> None:
        self.seats: Optional[str] = None
        self.engine: Optional[str] = None
        self.trip_computer: str = "No trip computer available"
        self.gps: str = "No GPS available"

    def set_seats(self, seats: int) -> None:
        self.seats = f"This car has {str(seats)} seats"

    def set_engine(self, engine: str) -> None:
        self.engine = f"This car has {engine} seats"

    def set_trip_computer(self) -> None:
        self.trip_computer = "Trip computer works by xyz"

    def set_gps(self) -> None:
        self.gps = "GPS works by xyz"
