# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed four core classes for PawPal+:
- **Task**: Represents a single pet care activity. It holds attributes like description, time, duration, priority, frequency, and completion status. It can mark itself complete or reschedule to a new time.
- **Pet**: Represents a pet owned by the user. It stores basic info (name, species, age) and a list of tasks. It can add, remove, and retrieve tasks.
- **Owner**: Represents the pet owner. It manages a list of pets and can retrieve tasks across all pets or for a specific pet.
- **Scheduler**: The brain of the system. It connects to the Owner to access all tasks, and handles sorting by time, filtering, conflict detection, and recurring task management.

The relationship is: Scheduler → manages → Owner → owns → Pet(s) → has → Task(s).


**b. Design changes**

One change I made during design was to the `get_all_tasks()` method in the `Owner` class. Originally I planned a separate method for getting all tasks, but I redesigned it as `get_pet_tasks(pet_name=None)` — a single flexible method that returns all tasks when no name is provided, or only the specified pet's tasks when a name is passed. This made the design cleaner and more reusable.

I also added a `due_date` attribute to the `Task` class during implementation. This was not in the original UML, but was needed to properly support recurring tasks — when a daily or weekly task is completed, the new task needs a calculated next due date based on today's date.


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers two main constraints: time (tasks are sorted chronologically so the owner knows what to do first) and priority (high-priority tasks like medications or vet appointments are ranked above low-priority ones like playtime). I decided time mattered most for the daily schedule view, since a pet owner needs to know when to act. Priority matters most when tasks conflict or when the owner needs to choose what to do first.

**b. Tradeoffs**

The scheduler only detects exact time matches as conflicts. For example, two tasks both at "09:00" will trigger a warning, but a 60-minute task at "09:00" and a task at "09:30" would not be flagged even though they overlap. This tradeoff keeps the logic simple and fast, which is reasonable for a basic pet care app where tasks are generally short and owners can manually adjust if needed.

---

## 3. AI Collaboration

**a. How you used AI**

I used GitHub Copilot Chat throughout the project by referencing #file:pawpal_system.py in every prompt, which gave Copilot the context it needed to generate accurate code. The most helpful prompts were specific and action-oriented, such as "implement the methods in the Task class" or "add save_to_json and load_from_json to the Owner class." I also used Copilot to generate test cases and add docstrings automatically.

**b. Judgment and verification**

One moment where I did not accept the AI suggestion as-is was in handle_recurring_tasks(). Copilot's first version used timedelta on the "HH:MM" time string instead of the actual date, which meant adding "1 day" had no real effect on scheduling. I recognized the logic error, rejected the suggestion, and asked Copilot to fix it by using datetime.now().date() as the base. I verified the fix by running main.py and confirming the new task showed the correct next-day due date.

---

## 4. Testing and Verification

**a. What you tested**

I tested five core behaviors: task completion status, task addition count, chronological sorting, recurring task creation, and conflict detection. These tests are important because they verify the core logic that the scheduler relies on — if any of these break, the entire daily schedule would be unreliable.

**b. Confidence**

Confidence level: ⭐⭐⭐⭐ (4/5). The core behaviors all pass. Edge cases I would test next include: a pet with no tasks, two recurring tasks completing at the same time, and invalid time formats like "8:00" instead of "08:00".

---

## 5. Reflection

**a. What went well**

I am most satisfied with the Scheduler class, particularly the algorithmic methods like weighted_sort() and find_next_available_slot(). These methods make the app genuinely useful rather than just a simple task list.

**b. What you would improve**

If I had another iteration, I would improve the UI to allow users to mark tasks as complete directly in the browser, and add the ability to add multiple pets from the UI instead of only through code.

**c. Key takeaway**

The most important thing I learned is that AI is most effective when you act as the architect — defining the structure and requirements clearly — and let AI handle the implementation details. Without a clear design upfront, AI-generated code can be inconsistent or miss key relationships between classes.
