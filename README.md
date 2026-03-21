# Лабораторная работа №1. Источники задач и контракты

## Цель работы

Освоить duck typing и контрактное программирование на примере источников
задач.Была реализована подсистема приёма задач в платформе
обработки задач. Задачи могут поступать из различных источников, не связанных
наследованием, но обязанных реализовывать единый поведенческий контракт (наличие метода get_tasks)

## Структура проекта

 <pre>
laba_mai1/
    ├── src/
    │   ├── __init__.py
    │   ├── task.py
    │   ├── protocol.py
    │   ├── sources.py
    │   ├── validate.py
    │   ├── api_client.py
    │   └── main.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_protocol.py
    │   ├── test_sources.py
    │   └──test_validate.py
    │
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── pyproject.toml
    ├── requirements.txt
    ├── uv.lock
    ├── README.md
    └── report.pdf
</pre>

## Источники задач

В рамках лабораторной работы были реализованы 4 источника задач:

### 1. FileSource

```python
class FileSource:
    def __init__(self, filename: str):
        self.filename = filename

    def get_tasks(self) -> list[Task]:
        return [Task(id=1, payload="meow1"), Task(id=2, payload="meow2")]
```

### 2. GeneratorSource

```python
class GeneratorSource:
    def __init__(self, count: int):
        self.count = count

    def get_tasks(self) -> list[Task]:
        return [Task(id=i, payload=f"generated_task_{i}") for i in range(self.count)]
```

### 3.APISource

```python
class APISource:
    def __init__(self, url: str):
        self.url = url.strip()

    def get_tasks(self) -> list[Task]:
        return [
            Task(id=1, payload={"status": 200}),
            Task(id=2, payload={"status": 505}),
            Task(id=3, payload={"status": "not found", "code": 400})
        ]
```

### 4.IncorrectSource

```python
class IncorrectSource:
    def __init__(self, sample: str):
        self.sample = sample

    def not_get_tasks(self) -> list[Task]:
        return []
```
