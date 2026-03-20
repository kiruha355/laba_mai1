import pytest
from task import Task
from protocol import TaskSource
from validate import TaskValidate
from sources import FileSource, GeneratorSource, APISource, IncorrectSource


class TestValidate:

    def test_validator_creation(self):
        validator = TaskValidate()
        assert validator is not None
        assert len(validator.sources) == 0

    def test_add_file_source(self):
        validator = TaskValidate()
        source = FileSource("test.txt")
        validator.add_source(source)
        assert len(validator.sources) == 1

    def test_add_generator_source(self):
        validator = TaskValidate()
        source = GeneratorSource(3)
        validator.add_source(source)
        assert len(validator.sources) == 1

    def test_add_api_source(self):
        validator = TaskValidate()
        source = APISource("https://api.example.com")
        validator.add_source(source)
        assert len(validator.sources) == 1

    def test_add_multiple_sources(self):
        validator = TaskValidate()
        validator.add_source(FileSource("test.txt"))
        validator.add_source(GeneratorSource(3))
        validator.add_source(APISource("https://api.example.com"))
        assert len(validator.sources) == 3

    def test_add_incorrect_source_raises_error(self):
        validator = TaskValidate()
        source = IncorrectSource("test")
        with pytest.raises(TypeError):
            validator.add_source(source)

    def test_load_all_tasks(self):
        validator = TaskValidate()
        validator.add_source(FileSource("test.txt"))
        validator.add_source(GeneratorSource(2))
        tasks = validator.load_all_tasks()
        assert len(tasks) == 4

    def test_load_tasks_returns_list(self):
        validator = TaskValidate()
        validator.add_source(FileSource("test.txt"))
        tasks = validator.load_all_tasks()
        assert isinstance(tasks, list)

    def test_load_tasks_returns_task_objects(self):
        validator = TaskValidate()
        validator.add_source(FileSource("test.txt"))
        tasks = validator.load_all_tasks()
        for task in tasks:
            assert isinstance(task, Task)

    def test_all_added_sources_are_protocol(self):
        validator = TaskValidate()
        validator.add_source(FileSource("test.txt"))
        validator.add_source(GeneratorSource(3))
        for source in validator.sources:
            assert isinstance(source, TaskSource)