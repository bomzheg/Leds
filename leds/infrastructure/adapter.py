from dataclasses import dataclass

import OPi.GPIO as gpio
import typing

from leds.infrastructure.consts import PI_PC_MAPPING
from leds.interfaces import LedAdapter, ButtonAdapter, BoardAdapter
from leds.state import SystemState

COUNT = 7


class LedAdapterGPIO(LedAdapter):
    mapping = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }

    def turn_on(self, number: int) -> None:
        gpio.output(self.mapping[number], gpio.HIGH)

    def turn_off(self, number: int) -> None:
        gpio.output(self.mapping[number], gpio.LOW)

    def setup(self) -> None:
        assert len(self.mapping) == COUNT
        for led in self.mapping.values():
            gpio.setup(led, gpio.OUT)


class ButtonAdapterGPIO(ButtonAdapter):
    mapping = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }

    def is_pressed(self, number: int) -> bool:
        return typing.cast(bool, gpio.input(self.mapping[number]) == gpio.HIGH)

    def setup(self) -> None:
        assert len(self.mapping) == COUNT
        for button in self.mapping.values():
            gpio.setup(button, gpio.IN)


@dataclass
class BoardAdapterGPIO(BoardAdapter):
    leds: LedAdapter
    buttons: ButtonAdapter

    def setup(self) -> None:
        gpio.cleanup()
        gpio.setmode(PI_PC_MAPPING)
        gpio.setwarnings(True)
        self.leds.setup()
        self.buttons.setup()

    def get_pressed(self) -> typing.Optional[int]:
        for i in range(COUNT):
            if self.buttons.is_pressed(i):
                return i
        return None

    def to_state(self, state: SystemState) -> None:
        pass

    def cleanup(self) -> None:
        gpio.cleanup()


def create_board_adapter() -> BoardAdapter:
    leds = LedAdapterGPIO()
    buttons = ButtonAdapterGPIO()
    board = BoardAdapterGPIO(leds=leds, buttons=buttons)
    return board
