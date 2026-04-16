from laba2.src.task import Task
from laba3.src.iterator import TaskIterator


class TaskQueue:
    """Очередь задач"""

    def __init__(self):
        self._tasks: list[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def __len__(self) -> int:
        return len(self._tasks)

    def __iter__(self) -> TaskIterator:
        return TaskIterator(self._tasks)

    def filter_by_status(self, status: str):
        for task in self._tasks:
            if task.status == status:
                yield task

    def filter_by_priority(self, min_priority: int):
        for task in self._tasks:
            if task.priority >= min_priority:
                yield task

    def stream(self, *filters):
        result = iter(self._tasks)
        for f in filters:
            result = f(result)
        return result