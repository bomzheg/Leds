from __future__ import annotations
from typing import Protocol

from leds import dto
from leds.state import SystemState


def process(
    state: SystemState,
    event: dto.NewState,
    board: BoardAdapter,
) -> None:
    for pressed in event.buttons:
        if pressed:
            state.on_press_led(pressed)
            board.to_state(state, event)
            return


class LedAdapter(Protocol):
    def turn_on(self, number: int) -> None:
        raise NotImplementedError

    def turn_off(self, number: int) -> None:
        raise NotImplementedError

    def check_state(self, numer: int) -> bool:
        raise NotImplementedError

    def setup(self) -> None:
        raise NotImplementedError


class ButtonAdapter(Protocol):
    def is_pressed(self, number: int) -> bool:
        raise NotImplementedError

    def setup(self) -> None:
        raise NotImplementedError


class BoardAdapter(Protocol):
    def setup(self) -> None:
        raise NotImplementedError

    def get_new_state(self) -> dto.NewState:
        raise NotImplementedError

    def to_state(self, state: SystemState, event: dto.NewState) -> None:
        raise NotImplementedError
