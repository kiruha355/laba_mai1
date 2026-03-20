from dataclasses import dataclass
from typing import Any


@dataclass
class Task:
    """Произвольная задача"""
    id: int
    payload: Any
