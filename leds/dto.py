from dataclasses import dataclass
from typing import List


@dataclass
class NewState:
    leds: List[bool]
    buttons: List[bool]
