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

    def mark_complete(self):
        pass

    def reschedule(self, new_time: str):
        pass


@dataclass
class Pet:
    name: str
    species: str               # "dog" / "cat" / "other"
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task_id: str):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet_name: str):
        pass

    def get_pet_tasks(self, pet_name: Optional[str] = None):
        # pet_name=None 
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_daily_schedule(self):
        pass

    def sort_by_time(self):
        pass

    def filter_tasks(self, pet_name: Optional[str] = None, is_complete: Optional[bool] = None):
        pass

    def detect_conflicts(self):
        pass

    def handle_recurring_tasks(self):
        pass