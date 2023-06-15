from dataclasses import dataclass
from typing import List


COUNT = 5


@dataclass
class LedState:
    on: bool

    def reset(self) -> None:
        self.on = False

    def turn_on(self) -> None:
        self.on = True

    def __repr__(self) -> str:
        result = "<Led "
        result += "1" if self.on else "0"
        result += ">"
        return result


@dataclass
class SystemState:
    leds: List[LedState]

    def on_press_led(self, number: int) -> None:
        for led in self.leds[:number]:
            if not led.on:
                self.reset_state()
                return
        for led in self.leds[number + 1 :]:
            if led.on:
                self.reset_state()
                return
        self.leds[number].turn_on()

    def reset_state(self) -> None:
        for led in self.leds:
            led.reset()

    def __repr__(self) -> str:
        result = "<System "
        for led in self.leds:
            result += "1" if led.on else "0"
        result += ">"
        return result


def create_system() -> SystemState:
    return SystemState([LedState(False) for _ in range(COUNT)])
