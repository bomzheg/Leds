from __future__ import annotations

from leds.interfaces import BoardAdapter
from leds.state import SystemState


def process(
    state: SystemState,
    pressed: int,
    board: BoardAdapter,
) -> None:
    state.on_press_led(pressed)
    board.to_state(state)
