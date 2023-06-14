#!/usr/bin/env python3
import logging
import time

import OPi.GPIO as gpio  # type: ignore[import]

from .infrastructure.consts import PI_PC_MAPPING

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
LED_PIN = 7
BUTTON_PIN = 16


def main() -> None:
    gpio.cleanup()
    gpio.setwarnings(True)
    try:
        gpio.setmode(PI_PC_MAPPING)
        gpio.setup(LED_PIN, gpio.OUT)
        gpio.output(LED_PIN, gpio.LOW)
        gpio.setup(BUTTON_PIN, gpio.IN)
        logger.warning("configured")
        main_loop()
    finally:
        gpio.cleanup()
        logger.warning("finished")


def main_loop() -> None:
    while True:
        if gpio.input(BUTTON_PIN) == gpio.LOW:
            timeout = 0.1
            logger.debug("key pressed")
        else:
            timeout = 0.5
        gpio.output(LED_PIN, gpio.HIGH)
        time.sleep(timeout)
        gpio.output(LED_PIN, gpio.LOW)
        time.sleep(timeout)


if __name__ == "__main__":
    main()
