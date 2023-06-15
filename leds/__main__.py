#!/usr/bin/env python3
import logging
import time
from typing import NoReturn

from leds import app
from leds.infrastructure.adapter import create_board_adapter
from leds.interfaces import BoardAdapter
from leds.state import create_system, SystemState


logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)


def main() -> NoReturn:
    board = create_board_adapter()
    board.setup()
    state = create_system()
    try:
        logger.warning("started")
        main_loop(board, state)
    finally:
        board.cleanup()
        logger.warning("finished")


def main_loop(board: BoardAdapter, state: SystemState) -> NoReturn:
    while True:
        time.sleep(0.05)
        pressed = board.get_pressed()
        if pressed is None:
            continue
        logger.info("got pressed button %s", pressed)
        app.process(state, pressed, board)


if __name__ == "__main__":
    main()
