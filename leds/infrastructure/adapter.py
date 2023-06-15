from dataclasses import dataclass

import OPi.GPIO as gpio
import typing

from leds.infrastructure.consts import PI_PC_MAPPING
from leds.interfaces import LedAdapter, ButtonAdapter, BoardAdapter
from leds.state import SystemState, COUNT


class LedAdapterGPIO(LedAdapter):
    mapping = {
        0: 7,
        1: 12,
        2: 18,
        3: 26,
        4: 29,
    }

    def turn_on(self, number: int) -> None:
        gpio.output(self.mapping[number], gpio.HIGH)

    def turn_off(self, number: int) -> None:
        gpio.output(self.mapping[number], gpio.LOW)

    def setup(self) -> None:
        assert len(self.mapping) == COUNT
        for led in self.mapping.values():
            gpio.setup(led, gpio.OUT)
            gpio.output(led, gpio.LOW)


class ButtonAdapterGPIO(ButtonAdapter):
    mapping = {
        0: 31,
        1: 33,
        2: 35,
        3: 37,
        4: 16,
    }

    def is_pressed(self, number: int) -> bool:
        if number == 4:
            return typing.cast(bool, gpio.input(self.mapping[number]) == gpio.LOW)
        return typing.cast(bool, gpio.input(self.mapping[number]) == gpio.HIGH)

    def setup(self) -> None:
        assert len(self.mapping) == COUNT
        for button in self.mapping.values():
            gpio.setup(button, gpio.IN)
            gpio.output(button, gpio.LOW)


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
        for i, led in enumerate(state.leds):
            if led.on:
                self.leds.turn_on(i)
            else:
                self.leds.turn_off(i)

    def cleanup(self) -> None:
        gpio.cleanup()


def create_board_adapter() -> BoardAdapter:
    leds = LedAdapterGPIO()
    buttons = ButtonAdapterGPIO()
    board = BoardAdapterGPIO(leds=leds, buttons=buttons)
    return board
