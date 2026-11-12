
from vehicles.car import Car
from vehicles.bike import Bike
from vehicles.bus import Bus
from vehicles.emergency_vehicle import EmergencyVehicle

from traffic_exceptions import InvalidVehicleError
from logger import get_logger


logger = get_logger(__name__)


class VehicleFactory:
    """Creates vehicle objects based on their category."""

    @staticmethod
    def create_vehicle(vehicle_type: str, vehicle_id: str, speed: float, **kwargs):
        if not isinstance(vehicle_type, str):
            raise InvalidVehicleError(
                "Vehicle type must be a string."
            )

        vehicle_type = vehicle_type.strip().upper()

        try:
            if vehicle_type == "CAR":
                vehicle = Car(
                    vehicle_id,
                    speed,
                    seats=kwargs.get("seats", 5)
                )

            elif vehicle_type == "BIKE":
                vehicle = Bike(
                    vehicle_id,
                    speed,
                    has_pillion=kwargs.get("has_pillion", False)
                )

            elif vehicle_type == "BUS":
                if "passenger_capacity" not in kwargs:
                    raise InvalidVehicleError(
                        "Bus requires passenger_capacity."
                    )

                vehicle = Bus(
                    vehicle_id,
                    speed,
                    passenger_capacity=kwargs["passenger_capacity"]
                )

            elif vehicle_type == "EMERGENCY":
                if "emergency_type" not in kwargs:
                    raise InvalidVehicleError(
                        "Emergency vehicle requires emergency_type."
                    )

                vehicle = EmergencyVehicle(
                    vehicle_id,
                    speed,
                    emergency_type=kwargs["emergency_type"]
                )

            else:
                raise InvalidVehicleError(
                    f"Unsupported vehicle type: {vehicle_type}"
                )

            logger.info(
                "Vehicle created successfully: %s",
                vehicle
            )

            return vehicle

        except (TypeError, ValueError) as error:
            logger.error(
                "Vehicle creation failed: %s",
                error
            )
            raise
