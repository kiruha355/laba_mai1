import pytest
from protocol import TaskSource
from sources import FileSource, GeneratorSource, APISource, IncorrectSource


class TestProtocol:

    def test_file_source_is_task_source(self):
        source = FileSource("test.txt")
        assert isinstance(source, TaskSource)

    def test_generator_source_is_task_source(self):
        source = GeneratorSource(3)
        assert isinstance(source, TaskSource)

    def test_api_source_is_task_source(self):
        source = APISource("https://api.example.com")
        assert isinstance(source, TaskSource)

    def test_incorrect_source_is_not_task_source(self):
        source = IncorrectSource("test")
        assert not isinstance(source, TaskSource)

    def test_file_source_class_is_task_source(self):
        assert issubclass(FileSource, TaskSource)

    def test_incorrect_source_class_is_not_task_source(self):
        assert not issubclass(IncorrectSource, TaskSource)

    def test_protocol_has_get_tasks(self):
        assert hasattr(TaskSource, 'get_tasks')
