
from vehicles.base_vehicle import Vehicle
from traffic_exceptions import InvalidVehicleError


class Car(Vehicle):
    """Represents a passenger car."""

    SPACE_OCCUPANCY = 2.5

    def __init__(self, vehicle_id: str, speed: float, seats: int = 5):
        super().__init__(vehicle_id, speed)
        self.seats = seats

    @property
    def vehicle_type(self) -> str:
        return "CAR"

    @property
    def seats(self) -> int:
        return self.__seats

    @seats.setter
    def seats(self, value: int):
        if isinstance(value, bool) or not isinstance(value, int):
            raise InvalidVehicleError("Seat count must be an integer.")

        if value <= 0:
            raise InvalidVehicleError("A car must have at least one seat.")

        self.__seats = value

    def calculate_space_occupancy(self) -> float:
        return self.SPACE_OCCUPANCY

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Seats: {self.seats}"
        )
