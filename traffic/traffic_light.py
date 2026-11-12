
from enum import Enum

from config import (
    DEFAULT_GREEN_TIME,
    DEFAULT_YELLOW_TIME,
    DEFAULT_RED_TIME
)
from traffic_exceptions import InvalidSignalTransitionError
from logger import get_logger


logger = get_logger(__name__)


class SignalState(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"


class TrafficLight:
    """Manages the state and timing of a traffic signal."""

    VALID_TRANSITIONS = {
        SignalState.RED: {SignalState.GREEN},
        SignalState.GREEN: {SignalState.YELLOW},
        SignalState.YELLOW: {SignalState.RED}
    }

    def __init__(self, light_id: str):
        if not isinstance(light_id, str) or not light_id.strip():
            raise ValueError("Traffic light ID cannot be empty.")

        self.__light_id = light_id.strip().upper()
        self.__state = SignalState.RED

        self.__durations = {
            SignalState.RED: DEFAULT_RED_TIME,
            SignalState.YELLOW: DEFAULT_YELLOW_TIME,
            SignalState.GREEN: DEFAULT_GREEN_TIME
        }

        logger.info(
            "Traffic light %s initialized in RED state.",
            self.__light_id
        )

    @property
    def light_id(self) -> str:
        return self.__light_id

    @property
    def state(self) -> SignalState:
        return self.__state

    @property
    def duration(self) -> int:
        return self.__durations[self.__state]

    def transition_to(self, new_state: SignalState) -> None:
        if not isinstance(new_state, SignalState):
            raise InvalidSignalTransitionError(
                "New state must be a valid SignalState."
            )

        allowed_states = self.VALID_TRANSITIONS[self.__state]

        if new_state not in allowed_states:
            raise InvalidSignalTransitionError(
                f"Cannot transition from {self.__state.value} "
                f"to {new_state.value}."
            )

        old_state = self.__state
        self.__state = new_state

        logger.info(
            "Traffic light %s changed from %s to %s.",
            self.__light_id,
            old_state.value,
            new_state.value
        )

    def is_green(self) -> bool:
        return self.__state == SignalState.GREEN

    def __str__(self) -> str:
        return (
            f"TrafficLight(ID={self.light_id}, "
            f"State={self.state.value}, "
            f"Duration={self.duration}s)"
        )
