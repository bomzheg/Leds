from typing import Dict, List

from leds.interfaces import ButtonAdapter


class ButtonAdapterMock(ButtonAdapter):
    def __init__(self) -> None:
        self.is_pressed_responses: Dict[int, List[bool]] = {}
        self.setup_calls = 0

    def is_pressed(self, number: int) -> bool:
        return self.is_pressed_responses[number].pop()

    def setup(self) -> None:
        self.setup_calls += 1
