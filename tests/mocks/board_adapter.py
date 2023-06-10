from dataclasses import dataclass, field
from typing import List

from leds import dto
from leds.interfaces import BoardAdapter
from leds.state import SystemState
from tests.mocks.button_adapter import ButtonAdapterMock
from tests.mocks.led_adapter import LedAdapterMock


@dataclass
class BoardAdapterMock(BoardAdapter):
    leds: LedAdapterMock
    buttons: ButtonAdapterMock

    setup_calls: int = 0
    new_state_results: List[dto.NewState] = field(default_factory=list)
    to_state_calls: List[SystemState] = field(default_factory=list)

    def setup(self) -> None:
        self.setup_calls += 1

    def get_new_state(self) -> dto.NewState:
        return self.new_state_results.pop()

    def to_state(self, state: SystemState) -> None:
        self.to_state_calls.append(state)
