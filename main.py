from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner(name="Jordan")

# Create pets
mochi = Pet(name="Mochi", species="dog", age=3)
luna = Pet(name="Luna", species="cat", age=2)

# Add pets to owner
owner.add_pet(mochi)
owner.add_pet(luna)

# Create tasks
walk_task = Task(task_id="1", description="Morning Walk", time="08:00", duration=30, priority="high", frequency="daily")
feed_task = Task(task_id="2", description="Feed Breakfast", time="07:30", duration=10, priority="medium", frequency="daily")
play_task = Task(task_id="3", description="Playtime", time="18:00", duration=20, priority="low", frequency="once")

# Add tasks to pets
mochi.add_task(walk_task)
mochi.add_task(feed_task)
luna.add_task(play_task)

# Add a conflict: two tasks at the same time
conflict_task1 = Task(task_id="4", description="Vet Appointment", time="09:00", duration=60, priority="high", frequency="once")
conflict_task2 = Task(task_id="5", description="Grooming", time="09:00", duration=45, priority="medium", frequency="once")
mochi.add_task(conflict_task1)
luna.add_task(conflict_task2)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule
print("Today's Schedule:")
schedule = scheduler.get_daily_schedule()
for task in schedule:
    print(f"- {task.time} | {task.description} (Pet: {'Mochi' if task in mochi.tasks else 'Luna'})")

# Test conflict detection
conflicts = scheduler.detect_conflicts()
if conflicts:
    print("\nConflicts detected:")
    for conflict in conflicts:
        print(conflict)
else:
    print("\nNo conflicts detected.")
