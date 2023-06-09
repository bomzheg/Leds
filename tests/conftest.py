import pytest

from leds.interfaces import LedAdapter, ButtonAdapter, BoardAdapter
from leds.state import LedState, SystemState
from tests.constants import TEST_COUNT
from tests.mocks.board_adapter import BoardAdapterMock
from tests.mocks.button_adapter import ButtonAdapterMock
from tests.mocks.led_adapter import LedAdapterMock


@pytest.fixture
def led_state() -> LedState:
    return LedState(False)


@pytest.fixture
def system_state() -> SystemState:
    return SystemState([LedState(False) for _ in range(TEST_COUNT)])


@pytest.fixture
def led_adapter() -> LedAdapter:
    return LedAdapterMock()


@pytest.fixture
def button_adapter() -> ButtonAdapter:
    return ButtonAdapterMock()


@pytest.fixture
def board_adapter(led_adapter: LedAdapterMock, button_adapter: ButtonAdapterMock) -> BoardAdapter:
    return BoardAdapterMock(leds=led_adapter, buttons=button_adapter)
