from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    task_id: str
    description: str
    time: str                  # "HH:MM"
    duration: int              # min
    priority: str              # "low" / "medium" / "high"
    frequency: str             # "once" / "daily" / "weekly"
    is_complete: bool = False
    due_date: Optional[str] = None       # "YYYY-MM-DD"

    def mark_complete(self):
        self.is_complete = True

    def reschedule(self, new_time: str):
        self.time = new_time


@dataclass
class Pet:
    name: str
    species: str               # "dog" / "cat" / "other"
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_id: str):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def get_tasks(self):
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet_name: str):
        self.pets = [pet for pet in self.pets if pet.name != pet_name]

    def get_pet_tasks(self, pet_name: Optional[str] = None):
        if pet_name is None:
            all_tasks = []
            for pet in self.pets:
                all_tasks.extend(pet.get_tasks())
            return all_tasks
        else:
            for pet in self.pets:
                if pet.name == pet_name:
                    return pet.get_tasks()
            return []


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_daily_schedule(self):
        tasks = self.owner.get_pet_tasks()
        return self.sort_by_time(tasks)

    def sort_by_time(self, tasks=None):
        if tasks is None:
            tasks = self.owner.get_pet_tasks()
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, pet_name: Optional[str] = None, is_complete: Optional[bool] = None):
        tasks = self.owner.get_pet_tasks(pet_name)
        if is_complete is not None:
            tasks = [task for task in tasks if task.is_complete == is_complete]
        return tasks

    def detect_conflicts(self):
        tasks = self.owner.get_pet_tasks()
        time_map = {}
        conflicts = []
        for task in tasks:
            if task.time in time_map:
                conflicts.append(f"Conflict: '{task.description}' and '{time_map[task.time].description}' are both scheduled at {task.time}.")
            else:
                time_map[task.time] = task
        return conflicts

    def handle_recurring_tasks(self):
        from datetime import datetime, timedelta
        new_tasks = []
        today = datetime.now().date()
        for pet in self.owner.pets:
            for task in pet.get_tasks():
                if task.is_complete and task.frequency in ("daily", "weekly"):
                    if task.frequency == "daily":
                        next_due_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")
                    else:
                        next_due_date = (today + timedelta(days=7)).strftime("%Y-%m-%d")
                    new_task = Task(
                        task_id=task.task_id + "_recurring",
                        description=task.description,
                        time=task.time,
                        duration=task.duration,
                        priority=task.priority,
                        frequency=task.frequency,
                        is_complete=False,
                        due_date=next_due_date
                    )
                    new_tasks.append((pet, new_task))
        for pet, task in new_tasks:
            pet.add_task(task)
        return new_tasks