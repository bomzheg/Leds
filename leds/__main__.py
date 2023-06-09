#!/usr/bin/env python3
import time

from leds import app
from leds.adapter import BoardAdapterGPIO, LedAdapterGPIO, ButtonAdapterGPIO
from leds.state import create_system


def main() -> None:
    leds = LedAdapterGPIO()
    buttons = ButtonAdapterGPIO()
    board = BoardAdapterGPIO(leds=leds, buttons=buttons)
    board.setup()
    state = create_system()

    while True:
        time.sleep(0.05)
        event = board.get_new_state()
        app.process(state, event, board)


if __name__ == "__main__":
    main()
