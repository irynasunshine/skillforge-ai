from src.core.scheduler import calculate_completion_percentage, distribute_tasks_by_week


def _make_task(completed: bool):
    class FakeTask:
        pass
    t = FakeTask()
    t.completed = completed
    return t


def test_completion_percentage_empty():
    assert calculate_completion_percentage([]) == 0.0


def test_completion_percentage_all_done():
    tasks = [_make_task(True)] * 4
    assert calculate_completion_percentage(tasks) == 100.0


def test_completion_percentage_half():
    tasks = [_make_task(True), _make_task(False)]
    assert calculate_completion_percentage(tasks) == 50.0


def test_distribute_tasks_by_week():
    tasks = [{"title": f"Task {i}", "week": 0} for i in range(8)]
    result = distribute_tasks_by_week(tasks, total_weeks=4)
    weeks = [t["week"] for t in result]
    assert min(weeks) >= 1
    assert max(weeks) <= 4
