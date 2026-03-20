from typing import List
from task import Task
from protocol import TaskSource


class TaskValidate:
    def __init__(self):
        self.sources: List[TaskSource] = []
        self.tasks: List[Task] = []

    def add_source(self, source: TaskSource) -> None:
        """Попытка добавить источник задач"""
        if not isinstance(source, TaskSource):
            raise TypeError("Источник должен соответствовать контракту")

        self.sources.append(source)

    def load_all_tasks(self) -> List[Task]:
        """Загрузка задач из источников"""

        for source in self.sources:
            tasks = source.get_tasks()
            self.tasks.extend(tasks)

        return self.tasks
