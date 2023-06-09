from typing import List

from leds.interfaces import LedAdapter


class LedAdapterMock(LedAdapter):
    def __init__(self) -> None:
        self.turn_on_calls: List[int] = []
        self.turn_off_calls: List[int] = []
        self.check_state_responses: List[bool] = []
        self.setup_calls = 0

    def turn_on(self, number: int) -> None:
        self.turn_on_calls.append(number)

    def turn_off(self, number: int) -> None:
        self.turn_off_calls.append(number)

    def check_state(self, numer: int) -> bool:
        return self.check_state_responses.pop()

    def setup(self) -> None:
        self.setup_calls += 1
