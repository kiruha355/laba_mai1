from typing import Protocol, runtime_checkable
from task import Task


@runtime_checkable
class TaskSource(Protocol):
    """Проверяет,подходящий ли это источкник по наличию метода get_tasks"""

    def get_tasks(self) -> list[Task]:
        "Список задач"
        pass
