import pytest
from laba2.src.task import Task
from laba3.src.queue import TaskQueue


def make_task(priority=5, status="pending", description="test"):
    task = Task(description=description, priority=priority, payload=None)
    task.status = status
    return task



class TestTaskQueue:
    def test_empty_queue_has_zero_length(self):
        queue = TaskQueue()
        assert len(queue) == 0

    def test_add_increases_length(self):
        queue = TaskQueue()
        queue.add(make_task())
        assert len(queue) == 1

    def test_add_multiple_tasks(self):
        queue = TaskQueue()
        queue.add(make_task())
        queue.add(make_task())
        queue.add(make_task())
        queue.add(make_task())
        queue.add(make_task())
        assert len(queue) == 5


class TestIteration:
    def test_for_loop_iterates_all_tasks(self):
        queue = TaskQueue()
        task1 = make_task(priority=1)
        task2 = make_task(priority=2)
        queue.add(task1)
        queue.add(task2)
        result = []
        for task in queue:
            result.append(task)
        assert result == [task1, task2]

    def test_empty_queue_iteration(self):
        queue = TaskQueue()
        result = list(queue)
        assert result == []

    def test_sum_of_priorities(self):
        queue = TaskQueue()
        queue.add(make_task(priority=3))
        queue.add(make_task(priority=7))
        total = sum(task.priority for task in queue)
        assert total == 10



class TestIterator:
    def test_iterator_raises_stop_iteration(self):
        queue = TaskQueue()
        queue.add(make_task())
        iterator = iter(queue)
        next(iterator)
        with pytest.raises(StopIteration):
            next(iterator)

    def test_each_iter_returns_new_iterator(self):
        queue = TaskQueue()
        queue.add(make_task())
        iter1 = iter(queue)
        iter2 = iter(queue)
        assert iter1 is not iter2



class TestFilterByStatus:
    def test_filter_returns_only_pending(self):
        queue = TaskQueue()
        task1 = make_task(status="pending")
        task2 = make_task(status="running")
        task3 = make_task(status="pending")
        queue.add(task1)
        queue.add(task2)
        queue.add(task3)
        result = list(queue.filter_by_status("pending"))
        assert result == [task1, task3]

    def test_filter_returns_empty_if_no_match(self):
        queue = TaskQueue()
        queue.add(make_task(status="pending"))
        result = list(queue.filter_by_status("done"))
        assert result == []



class TestFilterByPriority:
    def test_filter_returns_tasks_above_min(self):
        queue = TaskQueue()
        task1 = make_task(priority=3)
        task2 = make_task(priority=7)
        task3 = make_task(priority=5)
        queue.add(task1)
        queue.add(task2)
        queue.add(task3)
        result = list(queue.filter_by_priority(5))
        assert task2 in result
        assert task3 in result
        assert task1 not in result

    def test_filter_returns_empty_if_no_match(self):
        queue = TaskQueue()
        queue.add(make_task(priority=2))
        result = list(queue.filter_by_priority(5))
        assert result == []


class TestStream:
    def test_stream_with_no_filters_returns_all(self):
        queue = TaskQueue()
        queue.add(make_task(priority=5, status="pending"))
        queue.add(make_task(priority=3, status="running"))
        result = list(queue.stream())
        assert len(result) == 2

    def test_stream_with_one_filter(self):
        queue = TaskQueue()
        task1 = make_task(priority=5, status="pending")
        task2 = make_task(priority=3, status="running")
        queue.add(task1)
        queue.add(task2)

        def only_pending(tasks):
            for task in tasks:
                if task.status == "pending":
                    yield task

        result = list(queue.stream(only_pending))
        assert result == [task1]

    def test_stream_with_two_filters(self):
        queue = TaskQueue()
        task1 = make_task(priority=5, status="pending")
        task2 = make_task(priority=3, status="pending")
        task3 = make_task(priority=7, status="running")
        queue.add(task1)
        queue.add(task2)
        queue.add(task3)

        def only_pending(tasks):
            for task in tasks:
                if task.status == "pending":
                    yield task

        def only_high(tasks):
            for task in tasks:
                if task.priority >= 5:
                    yield task

        result = list(queue.stream(only_pending, only_high))
        assert result == [task1]