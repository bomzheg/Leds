from dataclasses import dataclass, field
from typing import List

import typing

from leds.interfaces import BoardAdapter
from leds.state import SystemState
from tests.mocks.button_adapter import ButtonAdapterMock
from tests.mocks.led_adapter import LedAdapterMock


@dataclass
class BoardAdapterMock(BoardAdapter):
    leds: LedAdapterMock
    buttons: ButtonAdapterMock

    setup_calls: int = 0
    cleanup_calls: int = 0
    to_state_calls: List[SystemState] = field(default_factory=list)
    get_pressed_responses: List[int] = field(default_factory=list)

    def setup(self) -> None:
        self.setup_calls += 1

    def to_state(self, state: SystemState) -> None:
        self.to_state_calls.append(state)

    def get_pressed(self) -> typing.Optional[int]:
        return self.get_pressed_responses.pop()

    def cleanup(self) -> None:
        self.cleanup_calls += 1
