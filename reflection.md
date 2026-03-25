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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

Confidence level: ⭐⭐⭐⭐ (4/5). The core behaviors all pass. Edge cases I would test next include: a pet with no tasks, two recurring tasks completing at the same time, and invalid time formats like "8:00" instead of "08:00".

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
