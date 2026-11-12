
from abc import ABC, abstractmethod

from traffic.intersection import Intersection


class TrafficController(ABC):
    """Abstract base class for traffic control strategies."""

    def __init__(self, intersection: Intersection):
        if not isinstance(intersection, Intersection):
            raise TypeError(
                "Controller requires a valid Intersection object."
            )

        self._intersection = intersection

    @property
    def intersection(self) -> Intersection:
        return self._intersection

    @abstractmethod
    def calculate_green_time(self, road_id: str) -> int:
        """Calculate the green signal duration for a road."""
        pass

    @abstractmethod
    def select_next_road(self) -> str:
        """Select the next road that should receive a green signal."""
        pass

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(Intersection={self.intersection.intersection_id})"
        )
