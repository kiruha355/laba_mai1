import urllib.request
import json
import uuid
import random
from src.task import Task


class APIClient:
    """Клиент для http запроса"""

    URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.client_id = str(uuid.uuid4())
        self.name = "Meow"
        self.task_limit = random.randint(1, 10)
        print(f"Клиент: {self.name}, id: {self.client_id}, задач: {self.task_limit}")

    def create_user(self) -> dict:
        """Создает пользователя через запрос"""
        data = json.dumps({
            "name": self.name,
            "client_id": self.client_id
        }).encode("utf-8")

        req = urllib.request.Request(
            url=f"{self.URL}/users",
            data=data,
            headers={"Content-Type": "application/json", "User-Agent": "Google"},
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=5) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result

