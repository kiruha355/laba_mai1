from task import Task


class FileSource:
    def __init__(self, filename: str):
        self.filename = filename

    def get_tasks(self) -> list[Task]:
        return [
            Task(id=1, payload="meow1"),
            Task(id=2, payload="meow2"),
        ]


class GeneratorSource:
    def __init__(self, count: int):
        self.count = count

    def get_tasks(self) -> list[Task]:
        return [
            Task(id=i, payload=f"generated_task_{i}")
            for i in range(self.count)
        ]


class APISource:
    def __init__(self, url: str):
        self.url = url

    def get_tasks(self) -> list[Task]:
        return [
            Task(id=1, payload={"status": 200}),
            Task(id=2, payload={"status": 505}),
            Task(id=3, payload={"status": "not found", "code": 400}),
        ]


class IncorrectSource:
    def __init__(self, sample: str):
        self.sample = sample

    def not_get_tasks(self) -> list[Task]:
        return []
