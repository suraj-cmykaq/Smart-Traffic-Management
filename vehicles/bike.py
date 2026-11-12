
from vehicles.base_vehicle import Vehicle
from traffic_exceptions import InvalidVehicleError


class Bike(Vehicle):
    """Represents a two-wheeler."""

    SPACE_OCCUPANCY = 1.0

    def __init__(self, vehicle_id: str, speed: float, has_pillion: bool = False):
        super().__init__(vehicle_id, speed)
        self.has_pillion = has_pillion

    @property
    def vehicle_type(self) -> str:
        return "BIKE"

    @property
    def has_pillion(self) -> bool:
        return self.__has_pillion

    @has_pillion.setter
    def has_pillion(self, value: bool):
        if not isinstance(value, bool):
            raise InvalidVehicleError(
                "Pillion status must be True or False."
            )

        self.__has_pillion = value

    def calculate_space_occupancy(self) -> float:
        return self.SPACE_OCCUPANCY

    def __str__(self) -> str:
        status = "Yes" if self.has_pillion else "No"

        return (
            f"{super().__str__()} | "
            f"Pillion: {status}"
        )
