class TrafficManagementError(Exception):
    """Base exception for the traffic management system."""
    pass


class InvalidVehicleError(TrafficManagementError):
    """Raised when vehicle data is invalid."""
    pass


class DuplicateVehicleError(TrafficManagementError):
    """Raised when a vehicle ID already exists."""
    pass


class QueueCapacityError(TrafficManagementError):
    """Raised when a traffic queue reaches its capacity."""
    pass


class InvalidSignalTransitionError(TrafficManagementError):
    """Raised when an invalid signal transition is attempted."""
    pass


class DataPersistenceError(TrafficManagementError):
    """Raised when traffic data cannot be saved or loaded."""
    pass


class ConfigurationError(TrafficManagementError):
    """Raised when system configuration is invalid."""
    pass