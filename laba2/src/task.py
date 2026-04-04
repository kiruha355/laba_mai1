from datetime import datetime
from typing import Any
from uuid import uuid4
from .descriptors import PositiveInt, NotEmptyString
from .errors import InvalidStatusError

class Task:
    priority = PositiveInt()
    description = NotEmptyString()

    def __init__(self, description: str, priority: int, payload: Any) -> None:
        self.id = uuid4()
        self.description = description
        self.priority = priority
        self._status = "pending"
        self.payload = payload
        self.__dict__["created_at"] = datetime.now()

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value):
        if value not in ("pending", "running", "done"):
            raise InvalidStatusError(f"недопустимый статус: {value}")
        self._status = value

    @property
    def is_ready(self) -> bool:
        return self.status == "pending" and self.priority >= 5