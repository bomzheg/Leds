#!/usr/bin/env python3
import time

import RPi.GPIO as gpio  # type: ignore[import]


LED_PIN = 7
BUTTON_PIN = 1


def main() -> None:
    gpio.cleanup()
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(LED_PIN, gpio.OUT)
        gpio.output(LED_PIN, gpio.LOW)
        gpio.setup(BUTTON_PIN, gpio.IN)
        print("configured")
        main_loop()
    finally:
        gpio.cleanup()


def main_loop() -> None:
    while True:
        if gpio.input(BUTTON_PIN):
            timeout = 0.5
        else:
            timeout = 0.1
            print("key pressed")
        gpio.output(LED_PIN, gpio.HIGH)
        time.sleep(timeout)
        gpio.output(LED_PIN, gpio.LOW)
        time.sleep(timeout)


if __name__ == "__main__":
    main()
