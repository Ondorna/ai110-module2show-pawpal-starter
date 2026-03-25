import pytest
from pawpal_system import Task, Pet

def test_mark_complete_sets_true():
    task = Task(task_id="t1", description="Test", time="10:00", duration=10, priority="low", frequency="once")
    assert not task.is_complete
    task.mark_complete()
    assert task.is_complete

def test_add_task_increases_count():
    pet = Pet(name="Buddy", species="dog", age=4)
    initial_count = len(pet.tasks)
    task = Task(task_id="t2", description="Feed", time="08:00", duration=5, priority="medium", frequency="daily")
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1
