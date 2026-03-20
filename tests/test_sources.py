import pytest
from task import Task
from sources import FileSource, GeneratorSource, APISource, IncorrectSource
from protocol import TaskSource


class TestSources:

    def test_file_source(self):
        source = FileSource("meow.txt")
        tasks = source.get_tasks()

        assert len(tasks) == 2
        assert isinstance(tasks[0], Task)
        assert tasks[0].id == 1
        assert tasks[0].payload == "meow1"
        assert tasks[1].id == 2
        assert tasks[1].payload == "meow2"

    def test_generator_source(self):
        count = 3
        source = GeneratorSource(count)
        tasks = source.get_tasks()

        assert len(tasks) == count
        for i, task in enumerate(tasks):
            assert task.id == i
            assert task.payload == f"generated_task_{i}"

    def test_api_source(self):
        source = APISource("https://api.example.com")
        tasks = source.get_tasks()

        assert len(tasks) == 3
        assert isinstance(tasks[0], Task)
        assert tasks[0].id == 1
        assert tasks[0].payload == {"status": 200}
        assert tasks[1].payload == {"status": 505}
        assert tasks[2].payload == {"status": "not found", "code": 400}

    def test_incorrect_source(self):
        source = IncorrectSource("test")
        assert not hasattr(source, 'get_tasks')
        assert hasattr(source, 'not_get_tasks')

    def test_file_source_is_protocol(self):
        source = FileSource("test.txt")
        assert isinstance(source, TaskSource)

    def test_generator_source_is_protocol(self):
        source = GeneratorSource(5)
        assert isinstance(source, TaskSource)

    def test_api_source_is_protocol(self):
        source = APISource("https://api.example.com")
        assert isinstance(source, TaskSource)

    def test_generator_source_zero_count(self):
        source = GeneratorSource(0)
        tasks = source.get_tasks()
        assert len(tasks) == 0

    def test_file_source_returns_list(self):
        source = FileSource("test.txt")
        tasks = source.get_tasks()
        assert isinstance(tasks, list)

    def test_api_source_returns_list(self):
        source = APISource("https://api.example.com")
        tasks = source.get_tasks()
        assert isinstance(tasks, list)

    def test_all_tasks_have_id_and_payload(self):
        sources = [
            FileSource("test.txt"),
            GeneratorSource(3),
            APISource("https://api.example.com")
        ]
        for source in sources:
            tasks = source.get_tasks()
            for task in tasks:
                assert hasattr(task, 'id')
                assert hasattr(task, 'payload')