from leds import dto
from leds.adapter import BoardAdapter
from leds.state import SystemState


def process(
    state: SystemState,
    event: dto.NewState,
    board: BoardAdapter,
) -> None:
    for pressed in event.buttons:
        if pressed:
            state.on_press_led(pressed)
            board.to_state(state, event)
            return