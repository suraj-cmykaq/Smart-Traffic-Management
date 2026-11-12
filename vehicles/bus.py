
from vehicles.base_vehicle import Vehicle
from traffic_exceptions import InvalidVehicleError


class Bus(Vehicle):
    """Represents a public transport bus."""

    SPACE_OCCUPANCY = 5.0

    def __init__(
        self,
        vehicle_id: str,
        speed: float,
        passenger_capacity: int
    ):
        super().__init__(vehicle_id, speed)
        self.passenger_capacity = passenger_capacity

    @property
    def vehicle_type(self) -> str:
        return "BUS"

    @property
    def passenger_capacity(self) -> int:
        return self.__passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value: int):
        if isinstance(value, bool) or not isinstance(value, int):
            raise InvalidVehicleError(
                "Passenger capacity must be an integer."
            )

        if value <= 0:
            raise InvalidVehicleError(
                "Passenger capacity must be greater than zero."
            )

        self.__passenger_capacity = value

    def calculate_space_occupancy(self) -> float:
        return self.SPACE_OCCUPANCY

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Passenger Capacity: {self.passenger_capacity}"
        )
