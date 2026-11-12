
from vehicles.base_vehicle import Vehicle
from traffic_exceptions import InvalidVehicleError


class EmergencyVehicle(Vehicle):
    """Represents an emergency response vehicle."""

    SPACE_OCCUPANCY = 3.0
    PRIORITY_LEVEL = 10

    VALID_EMERGENCY_TYPES = {
        "AMBULANCE",
        "FIRE_TRUCK",
        "POLICE"
    }

    def __init__(
        self,
        vehicle_id: str,
        speed: float,
        emergency_type: str
    ):
        super().__init__(vehicle_id, speed)
        self.emergency_type = emergency_type

    @property
    def vehicle_type(self) -> str:
        return "EMERGENCY"

    @property
    def emergency_type(self) -> str:
        return self.__emergency_type

    @emergency_type.setter
    def emergency_type(self, value: str):
        if not isinstance(value, str):
            raise InvalidVehicleError(
                "Emergency type must be a string."
            )

        value = value.strip().upper()

        if value not in self.VALID_EMERGENCY_TYPES:
            raise InvalidVehicleError(
                f"Invalid emergency type: {value}"
            )

        self.__emergency_type = value

    def calculate_space_occupancy(self) -> float:
        return self.SPACE_OCCUPANCY

    def get_priority(self) -> int:
        return self.PRIORITY_LEVEL

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Emergency Type: {self.emergency_type} | "
            f"Priority: {self.get_priority()}"
        )
