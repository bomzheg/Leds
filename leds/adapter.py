from dataclasses import dataclass

import RPi.GPIO as gpio  # type: ignore[import]
import typing

from leds import dto
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

    def check_state(self, numer: int) -> bool:
        return typing.cast(bool, gpio.input(self.mapping[numer]) == gpio.HIGH)

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


@dataclass
class BoardAdapterGPIO(BoardAdapter):
    leds: LedAdapter
    buttons: ButtonAdapter

    def setup(self) -> None:
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        self.leds.setup()
        self.buttons.setup()

    def get_new_state(self) -> dto.NewState:
        leds = [self.leds.check_state(i) for i in range(COUNT)]
        buttons = [self.buttons.is_pressed(i) for i in range(COUNT)]
        return dto.NewState(leds=leds, buttons=buttons)

    def to_state(self, state: SystemState, event: dto.NewState) -> None:
        pass
