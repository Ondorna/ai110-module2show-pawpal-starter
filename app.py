import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
import uuid
import os

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(160deg, #fff0f6 0%, #fce4f5 50%, #ffe8f0 100%) !important;
}

/* Hide default header */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: #d63384;
    letter-spacing: 2px;
    margin-bottom: 0.2em;
    text-shadow: 2px 2px 8px #ffb6d5;
}

.main-subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #e683b0;
    margin-bottom: 2em;
}

/* Section title */
.section-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #c2185b;
    margin: 1.5em 0 0.5em 0;
    padding-left: 0.5em;
    border-left: 4px solid #f48fb1;
}

/* Task card */
.task-card {
    background: white;
    border-radius: 20px;
    padding: 1em 1.5em;
    margin-bottom: 0.8em;
    border: 1.5px solid #f8bbd0;
    box-shadow: 0 4px 15px rgba(233, 30, 99, 0.08);
    transition: transform 0.2s;
}

.task-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(233, 30, 99, 0.15);
}

.task-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #880e4f;
}

.task-meta {
    font-size: 0.9rem;
    color: #ad1457;
    margin-top: 0.3em;
}

.task-status {
    font-size: 0.85rem;
    margin-top: 0.3em;
    color: #c2185b;
}

/* Conflict warning */
.conflict-box {
    background: #fff0f3;
    border: 2px solid #f48fb1;
    border-radius: 15px;
    padding: 0.8em 1.2em;
    margin-bottom: 0.8em;
    color: #c2185b;
    font-weight: 600;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(90deg, #f06292, #e91e8c) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.6em 2em !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    box-shadow: 0 4px 15px rgba(233, 30, 99, 0.3) !important;
    transition: all 0.3s !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(233, 30, 99, 0.4) !important;
}

/* Input fields */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    border-radius: 12px !important;
    border: 1.5px solid #f48fb1 !important;
    background: #fff8fb !important;
    color: #880e4f !important;
}

/* Selectbox */
div[data-testid="stSelectbox"] > div,
div[data-testid="stSelectbox"] > div > div {
    border-radius: 12px !important;
    border: 1.5px solid #f48fb1 !important;
    background: #fff8fb !important;
    color: #880e4f !important;
}

/* Selectbox dropdown options */
div[data-baseweb="select"] * {
    background: #fff8fb !important;
    color: #880e4f !important;
}

/* Number input buttons */
div[data-testid="stNumberInput"] button {
    background: #f8bbd0 !important;
    color: #880e4f !important;
    border-radius: 8px !important;
    border: none !important;
}

/* Radio */
div[data-testid="stRadio"] label {
    color: #c2185b !important;
    font-weight: 600;
}

/* All input/selectbox labels */
label, .stTextInput label, .stNumberInput label,
.stSelectbox label, .stRadio label {
    color: #c2185b !important;
    font-weight: 600 !important;
}

/* Divider */
hr {
    border-color: #f8bbd0 !important;
}

/* Radio buttons */
div[data-testid="stRadio"] input[type="radio"] {
    accent-color: #e91e8c !important;
}

div[data-testid="stRadio"] label p {
    color: #c2185b !important;
    font-weight: 600 !important;
}

/* Top toolbar (Deploy button etc) */
div[data-testid="stToolbar"] * {
    color: #c2185b !important;
}

header button, header a {
    color: #c2185b !important;
}

/* Info box */
div[data-testid="stAlert"] {
    background: #fff0f6 !important;
    border: 1.5px solid #f48fb1 !important;
    border-radius: 15px !important;
    color: #c2185b !important;
}

div[data-testid="stAlert"] p {
    color: #c2185b !important;
}
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="main-title">🐾 PawPal+</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">🌸 Your cozy pet care planner — making every day special! 🌸</div>', unsafe_allow_html=True)

st.divider()

# Session state
if "owner" not in st.session_state:
    if os.path.exists("data.json"):
        st.session_state.owner = Owner.load_from_json("data.json")
    else:
        st.session_state.owner = Owner(name="Jordan")
        st.session_state.owner.add_pet(Pet(name="Mochi", species="dog", age=3))

# Owner and Pet Info
st.markdown('<div class="section-title">🏠 Owner & Pet Info</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    owner_name = st.text_input("👤 Owner name", value=st.session_state.owner.name)
    st.session_state.owner.name = owner_name
with col2:
    pet_name = st.text_input("🐾 Pet name", value=st.session_state.owner.pets[0].name if st.session_state.owner.pets else "Mochi")
with col3:
    species = st.selectbox("🐶 Species", ["dog", "cat", "other"])

pet = next((p for p in st.session_state.owner.pets if p.name == pet_name), None)
if not pet:
    pet = Pet(name=pet_name, species=species, age=1)
    st.session_state.owner.add_pet(pet)

st.divider()

# Add Task
st.markdown('<div class="section-title">✏️ Add a New Task</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("📝 Task title", value="Morning walk")
with col2:
    duration = st.number_input("⏱ Duration (min)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("⭐ Priority", ["low", "medium", "high"], index=2)

col4, col5 = st.columns(2)
with col4:
    time = st.text_input("🕐 Time (HH:MM)", value="08:00")
with col5:
    frequency = st.selectbox("🔁 Frequency", ["once", "daily", "weekly"])

if st.button("➕ Add Task", use_container_width=True):
    task = Task(
        task_id=str(uuid.uuid4()),
        description=task_title,
        time=time,
        duration=int(duration),
        priority=priority,
        frequency=frequency
    )
    pet.add_task(task)
    st.session_state.owner.save_to_json("data.json")
    st.success(f"🌸 Added **{task_title}** to **{pet.name}**!")

st.divider()

# Task list
priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}

sort_mode = st.radio(
    "📋 Sort tasks by:",
    ["By Time 🕐", "By Priority ⭐"],
    horizontal=True
)

if pet.tasks:
    st.markdown(f'<div class="section-title">🐾 {pet.name}\'s Tasks</div>', unsafe_allow_html=True)

    if sort_mode == "By Time 🕐":
        sorted_tasks = sorted(pet.tasks, key=lambda t: t.time)
    else:
        p_order = {"high": 0, "medium": 1, "low": 2}
        sorted_tasks = sorted(pet.tasks, key=lambda t: p_order.get(t.priority, 3))

    for t in sorted_tasks:
        emoji = priority_emoji.get(t.priority, "")
        status = "✅ Complete" if t.is_complete else "🔘 Pending"
        st.markdown(f"""
        <div class="task-card">
            <div class="task-title">{emoji} {t.description}</div>
            <div class="task-meta">🕐 {t.time} &nbsp;|&nbsp; ⏱ {t.duration} min &nbsp;|&nbsp; 🔁 {t.frequency.capitalize()}</div>
            <div class="task-status">{status} &nbsp;|&nbsp; Priority: {t.priority.capitalize()}</div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("🐾 No tasks yet — add one above!")

st.divider()

# Generate schedule
st.markdown('<div class="section-title">📅 Today\'s Schedule</div>', unsafe_allow_html=True)

if st.button("🌸 Generate Schedule", use_container_width=True):
    scheduler = Scheduler(st.session_state.owner)
    schedule = scheduler.get_daily_schedule()

    if schedule:
        for t in schedule:
            pet_owner = next((p.name for p in st.session_state.owner.pets if t in p.tasks), "?")
            emoji = priority_emoji.get(t.priority, "")
            status = "✅ Complete" if t.is_complete else "🔘 Pending"
            st.markdown(f"""
            <div class="task-card">
                <div class="task-title">{emoji} {t.description} <span style="float:right;font-size:0.9rem;color:#e683b0;">🐾 {pet_owner}</span></div>
                <div class="task-meta">🕐 {t.time} &nbsp;|&nbsp; ⏱ {t.duration} min &nbsp;|&nbsp; 🔁 {t.frequency.capitalize()}</div>
                <div class="task-status">{status} &nbsp;|&nbsp; Priority: {t.priority.capitalize()}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("🐾 No tasks scheduled yet!")

    # Conflict detection
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        st.markdown('<div class="section-title">⚠️ Conflicts Detected</div>', unsafe_allow_html=True)
        for warning in conflicts:
            st.markdown(f'<div class="conflict-box">⚠️ {warning}</div>', unsafe_allow_html=True)