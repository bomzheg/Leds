import pytest

from leds.state import LedState, SystemState
from tests.constants import TEST_COUNT


def test_led_state(led_state: LedState) -> None:
    led_state.turn_on()
    assert led_state.on
    led_state.reset()
    assert not led_state.on


@pytest.mark.parametrize("number", list(range(TEST_COUNT)))
def test_system_state_press_correct(system_state: SystemState, number: int) -> None:
    for led in system_state.leds[:number]:
        led.turn_on()
    system_state.on_press_led(number)
    assert all([led.on for led in system_state.leds[: number + 1]])
    assert all([not led.on for led in system_state.leds[number + 1 :]])


@pytest.mark.parametrize("number", list(range(1, TEST_COUNT)))
def test_system_state_press_first_wrong(system_state: SystemState, number: int) -> None:
    system_state.on_press_led(number)
    assert all([not led.on for led in system_state.leds])


@pytest.mark.parametrize("chain", list(range(1, TEST_COUNT)))
def test_system_state_pres_middle_wrong(system_state: SystemState, chain: int) -> None:
    wrongs = list(range(TEST_COUNT))
    wrongs.remove(chain - 1)  # last pressed
    wrongs.remove(chain)  # next correct
    assert len(wrongs) == TEST_COUNT - 2
    for wrong in wrongs:
        system_state.reset_state()
        for led in system_state.leds[:chain]:
            led.turn_on()
        system_state.on_press_led(wrong)
        assert all([not led.on for led in system_state.leds])
