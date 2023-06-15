from __future__ import annotations

from typing import Protocol

import typing

from leds.state import SystemState


class LedAdapter(Protocol):
    def turn_on(self, number: int) -> None:
        raise NotImplementedError

    def turn_off(self, number: int) -> None:
        raise NotImplementedError

    def setup(self) -> None:
        raise NotImplementedError


class ButtonAdapter(Protocol):
    def is_pressed(self, number: int) -> bool:
        raise NotImplementedError

    def setup(self) -> None:
        raise NotImplementedError


class BoardAdapter(Protocol):
    def setup(self) -> None:
        raise NotImplementedError

    def get_pressed(self) -> typing.Optional[int]:
        raise NotImplementedError

    def to_state(self, state: SystemState) -> None:
        raise NotImplementedError

    def cleanup(self) -> None:
        raise NotImplementedError
