
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from logger import get_logger


logger = get_logger(__name__)


@dataclass(frozen=True)
class TrafficEvent:
    """Stores information about an event in the traffic system."""

    event_type: str
    message: str
    source: str
    timestamp: datetime

    @classmethod
    def create(
        cls,
        event_type: str,
        message: str,
        source: str
    ):
        return cls(
            event_type=event_type,
            message=message,
            source=source,
            timestamp=datetime.now(timezone.utc)
        )


class TrafficObserver(ABC):
    """Abstract observer that receives traffic events."""

    @abstractmethod
    def update(self, event: TrafficEvent) -> None:
        pass


class TrafficSubject:
    """Maintains observers and broadcasts traffic events."""

    def __init__(self):
        self.__observers = []

    def attach(self, observer: TrafficObserver) -> None:
        if not isinstance(observer, TrafficObserver):
            raise TypeError(
                "Observer must inherit from TrafficObserver."
            )

        if observer in self.__observers:
            logger.warning("Observer is already registered.")
            return

        self.__observers.append(observer)

        logger.info(
            "Observer registered: %s",
            observer.__class__.__name__
        )

    def detach(self, observer: TrafficObserver) -> None:
        if observer not in self.__observers:
            logger.warning("Observer is not registered.")
            return

        self.__observers.remove(observer)

        logger.info(
            "Observer removed: %s",
            observer.__class__.__name__
        )

    def notify(self, event: TrafficEvent) -> None:
        if not isinstance(event, TrafficEvent):
            raise TypeError("A valid TrafficEvent is required.")

        for observer in tuple(self.__observers):
            try:
                observer.update(event)

            except Exception:
                logger.exception(
                    "Observer %s failed to process event.",
                    observer.__class__.__name__
                )

    @property
    def observer_count(self) -> int:
        return len(self.__observers)


class LoggingObserver(TrafficObserver):
    """Observer that records traffic events in the application log."""

    def update(self, event: TrafficEvent) -> None:
        logger.info(
            "TRAFFIC EVENT | Type: %s | Source: %s | Message: %s",
            event.event_type,
            event.source,
            event.message
        )


class ConsoleObserver(TrafficObserver):
    """Observer that displays traffic events in the terminal."""

    def update(self, event: TrafficEvent) -> None:
        print(
            f"[{event.timestamp.isoformat()}] "
            f"{event.event_type} | "
            f"{event.source} | "
            f"{event.message}"
        )
