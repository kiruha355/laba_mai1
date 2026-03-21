import urllib.request
import json
from src.task import Task


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
    URL = "https://jsonplaceholder.typicode.com/todos"

    def __init__(self, limit):
        self.url = f"{self.URL}?_limit={limit}"

    def get_tasks(self) -> list[Task]:
        with urllib.request.urlopen(self.url) as response:
            raw: list[dict] = json.loads(response.read().decode())

        return [
            Task(id=item["id"], payload=item["title"])
            for item in raw
        ]


class IncorrectSource:
    def __init__(self, sample: str):
        self.sample = sample

    def not_get_tasks(self) -> list[Task]:
        return []
