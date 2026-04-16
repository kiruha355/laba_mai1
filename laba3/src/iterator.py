class TaskIterator:
    """Итератор обхода задач"""

    def __init__(self, tasks: list):
        self._tasks = tasks
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._tasks):
            raise StopIteration
        task = self._tasks[self._index]
        self._index += 1
        return task