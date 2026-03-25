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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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

- What behaviors did you test?
- Why were these tests important?

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
