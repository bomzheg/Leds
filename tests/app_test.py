from leds import dto, app
from leds.state import SystemState
from tests.constants import TEST_COUNT
from tests.mocks.board_adapter import BoardAdapterMock


def test_app(system_state: SystemState, board_adapter: BoardAdapterMock) -> None:
    event = dto.NewState(
        leds=[False for _ in range(TEST_COUNT)], buttons=[False for _ in range(TEST_COUNT)]
    )
    app.process(system_state, event, board_adapter)
    assert all([not led.on for led in system_state.leds])
    assert not board_adapter.to_state_calls
