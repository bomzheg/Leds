#!/usr/bin/env python3
import time

from leds import app
from leds.infrastructure.adapter import BoardAdapterGPIO, LedAdapterGPIO, ButtonAdapterGPIO
from leds.state import create_system


def main() -> None:
    leds = LedAdapterGPIO()
    buttons = ButtonAdapterGPIO()
    board = BoardAdapterGPIO(leds=leds, buttons=buttons)
    board.setup()
    state = create_system()

    while True:
        time.sleep(0.05)
        pressed = board.get_pressed()
        if pressed is None:
            continue
        app.process(state, pressed, board)


if __name__ == "__main__":
    main()
