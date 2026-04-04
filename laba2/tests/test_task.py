import pytest
from src.task import Task
from src.errors import (
    InvalidTypeError,
    InvalidValueError,
    InvalidStatusError,
    TaskValidationError,
)


class TestTaskCreation:
    def test_valid_task_creation(self):
        task = Task(description="test", priority=5, payload="data")
        assert task.description == "test"
        assert task.priority == 5
        assert task.payload == "data"

    def test_id_is_set_automatically(self):
        task = Task(description="test", priority=5, payload=None)
        assert task.id is not None

    def test_two_tasks_have_different_ids(self):
        task1 = Task(description="test", priority=5, payload=None)
        task2 = Task(description="test", priority=5, payload=None)
        assert task1.id != task2.id

    def test_default_status_is_pending(self):
        task = Task(description="test", priority=5, payload=None)
        assert task.status == "pending"

    def test_created_at_is_set_automatically(self):
        from datetime import datetime
        task = Task(description="test", priority=5, payload=None)
        assert isinstance(task.created_at, datetime)


class TestPositiveInt:
    def test_priority_accepts_positive_int(self):
        task = Task(description="test", priority=3, payload=None)
        assert task.priority == 3

    def test_priority_raises_invalid_type_for_string(self):
        with pytest.raises(InvalidTypeError):
            Task(description="test", priority="low", payload=None)

    def test_priority_raises_invalid_type_for_float(self):
        with pytest.raises(InvalidTypeError):
            Task(description="test", priority=1.5, payload=None)

    def test_priority_raises_invalid_value_for_zero(self):
        with pytest.raises(InvalidValueError):
            Task(description="test", priority=0, payload=None)

    def test_priority_raises_invalid_value_for_negative(self):
        with pytest.raises(InvalidValueError):
            Task(description="test", priority=-5, payload=None)



class TestNotEmptyString:
    def test_description_accepts_valid_string(self):
        task = Task(description="valid", priority=1, payload=None)
        assert task.description == "valid"

    def test_description_raises_invalid_type_for_int(self):
        with pytest.raises(InvalidTypeError):
            Task(description=123, priority=1, payload=None)

    def test_description_raises_invalid_value_for_empty(self):
        with pytest.raises(InvalidValueError):
            Task(description="", priority=1, payload=None)

    def test_description_raises_invalid_value_for_whitespace(self):
        with pytest.raises(InvalidValueError):
            Task(description="   ", priority=1, payload=None)


class TestStatus:
    def test_status_accepts_done(self):
        task = Task(description="test", priority=1, payload=None)
        task.status = "done"
        assert task.status == "done"

    def test_status_accepts_pending(self):
        task = Task(description="test", priority=1, payload=None)
        task.status = "pending"
        assert task.status == "pending"

    def test_status_raises_invalid_status_on_update(self):
        task = Task(description="test", priority=1, payload=None)
        with pytest.raises(InvalidStatusError):
            task.status = "broken"




class TestIsReady:
    def test_is_ready_true_when_pending_and_priority_5(self):
        task = Task(description="test", priority=5, payload=None)
        assert task.is_ready is True

    def test_is_ready_true_when_pending_and_priority_above_5(self):
        task = Task(description="test", priority=9, payload=None)
        assert task.is_ready is True

    def test_is_ready_false_when_priority_below_5(self):
        task = Task(description="test", priority=4, payload=None)
        assert task.is_ready is False

    def test_is_ready_false_when_status_running(self):
        task = Task(description="test", priority=5, payload=None)
        task.status = "running"
        assert task.is_ready is False



class TestErrorHierarchy:
    def test_invalid_type_is_validation_error(self):
        assert issubclass(InvalidTypeError, TaskValidationError)

    def test_invalid_value_is_validation_error(self):
        assert issubclass(InvalidValueError, TaskValidationError)

    def test_invalid_status_is_validation_error(self):
        assert issubclass(InvalidStatusError, TaskValidationError)