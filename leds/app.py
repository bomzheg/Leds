from __future__ import annotations

import logging

from leds.interfaces import BoardAdapter
from leds.state import SystemState


logger = logging.getLogger(__name__)


def process(
    state: SystemState,
    pressed: int,
    board: BoardAdapter,
) -> None:
    logger.debug("state %s before pressing %s", state, pressed)
    state.on_press_led(pressed)
    logger.debug("state %s after pressing %s", state, pressed)
    board.to_state(state)
