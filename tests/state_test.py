import pytest

from leds.state import LedState, SystemState

TEST_COUNT = 7


@pytest.fixture
def led_state() -> LedState:
    return LedState(False)

@pytest.fixture
def system_state() -> SystemState:
    return SystemState([LedState(False) for _ in range(TEST_COUNT)])


def test_led_state(led_state: LedState) -> None:
    led_state.turn_on()
    assert led_state.on
    led_state.reset()
    assert not led_state.on


@pytest.mark.parametrize("number", list(range(TEST_COUNT, 1)))
def test_system_state_press_first_wrong(system_state: SystemState, number: int) -> None:
    system_state.on_press_led(number)
    assert all([not led.on for led in system_state.leds])

