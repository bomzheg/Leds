from leds import app
from leds.state import SystemState
from tests.mocks.board_adapter import BoardAdapterMock


def test_app(system_state: SystemState, board_adapter: BoardAdapterMock) -> None:
    app.process(system_state, 1, board_adapter)
    assert all([not led.on for led in system_state.leds])
    assert [system_state] == board_adapter.to_state_calls
