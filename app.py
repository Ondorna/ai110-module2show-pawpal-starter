import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
import uuid

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# Session state for Owner
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")
    # Add a default pet for demo
    st.session_state.owner.add_pet(Pet(name="Mochi", species="dog", age=3))

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name

pet_name = st.text_input("Pet name", value=st.session_state.owner.pets[0].name if st.session_state.owner.pets else "Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"], index=0)

# Ensure pet exists in owner's pets
pet = next((p for p in st.session_state.owner.pets if p.name == pet_name), None)
if not pet:
    pet = Pet(name=pet_name, species=species, age=1)
    st.session_state.owner.add_pet(pet)

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
time = st.text_input("Task time (HH:MM)", value="08:00")
frequency = st.selectbox("Frequency", ["once", "daily", "weekly"], index=0)

if st.button("Add task"):
    task = Task(
        task_id=str(uuid.uuid4()),
        description=task_title,
        time=time,
        duration=int(duration),
        priority=priority,
        frequency=frequency
    )
    pet.add_task(task)
    st.success(f"Added task '{task_title}' to {pet.name}.")

if pet.tasks:
    st.write(f"Current tasks for {pet.name}:")
    st.table([{k: getattr(t, k) for k in ['description', 'time', 'duration', 'priority', 'frequency', 'is_complete']} for t in pet.tasks])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    schedule = scheduler.get_daily_schedule()
    if schedule:
        st.write("### Today's Schedule")
        st.table([
            {
                "Task": t.description,
                "Time": t.time,
                "Pet": next((p.name for p in st.session_state.owner.pets if t in p.tasks), "?"),
                "Priority": t.priority,
                "Complete": t.is_complete
            }
            for t in schedule
        ])
    else:
        st.info("No tasks scheduled.")
    # Show conflicts
    conflicts = scheduler.detect_conflicts()
    for warning in conflicts:
        st.warning(warning)
