# =============================================================
# toDo — Flask (Python) Backend
# File: app.py
# =============================================================
# This file does everything on the server side:
#   1. Stores tasks in memory (a Python list)
#   2. Defines URL routes that the browser can visit
#   3. Renders the HTML template with live data
#   4. Handles Add / Toggle-done / Delete actions
# =============================================================

from flask import Flask, render_template, request, redirect, url_for

# Create the Flask application object
app = Flask(__name__)


# -------------------------------------------------------------
# DATA STORAGE
# A plain Python list of task dictionaries.
# ⚠️  Data is lost when the server restarts.
#     For real persistence use SQLite or a JSON file.
# -------------------------------------------------------------
tasks = [
    {
        "id": 1,
        "name": "Do 30 minutes of yoga 🧘",
        "description": "",
        "time": "07:30",
        "project": "Health",
        "group": "today",
        "priority": "p1",
        "done": False,
    },
    {
        "id": 2,
        "name": "Dentist appointment",
        "description": "",
        "time": "10:00",
        "project": "Personal",
        "group": "today",
        "priority": "",
        "done": False,
    },
    {
        "id": 3,
        "name": "Buy bread 🍞",
        "description": "Sourdough loaf",
        "time": "",
        "project": "Shopping",
        "group": "today",
        "priority": "",
        "done": False,
    },
    {
        "id": 4,
        "name": "Team standup meeting",
        "description": "",
        "time": "09:00",
        "project": "Work",
        "group": "upcoming",
        "priority": "p2",
        "done": False,
    },
    {
        "id": 5,
        "name": "Review project proposal",
        "description": "",
        "time": "14:00",
        "project": "Work",
        "group": "upcoming",
        "priority": "p1",
        "done": False,
    },
]

# Auto-incrementing counter for new task IDs
next_id = 6

# All available projects and their sidebar colours
PROJECT_COLORS = {
    "Personal": "#e03030",
    "Work":     "#7c3aed",
    "Shopping": "#0891b2",
    "Health":   "#16a34a",
}


# -------------------------------------------------------------
# HELPER
# -------------------------------------------------------------
def format_time(t):
    """
    Convert 24-hour string 'HH:MM' → 12-hour string '7:30 AM'.
    Returns an empty string if t is falsy.
    """
    if not t:
        return ""
    h, m = map(int, t.split(":"))
    ampm = "AM" if h < 12 else "PM"
    h12  = h % 12 or 12
    return f"{h12}:{m:02d} {ampm}"


# -------------------------------------------------------------
# ROUTES
# Each @app.route decorator maps a URL to a Python function.
# -------------------------------------------------------------

# GET /  →  Home page: render all tasks
@app.route("/")
def index():
    # ?view=today (default) or ?view=upcoming
    active_view = request.args.get("view", "today")
    if active_view not in ("today", "upcoming"):
        active_view = "today"

    # Filter tasks by group so the template can render two sections
    today    = [t for t in tasks if t["group"] == "today"]
    upcoming = [t for t in tasks if t["group"] == "upcoming"]

    return render_template(
        "index.html",
        today=today,
        upcoming=upcoming,
        active_view=active_view,
        project_colors=PROJECT_COLORS,
        all_projects=list(PROJECT_COLORS.keys()),
        format_time=format_time,     # pass helper so Jinja2 can call it
    )


# POST /add  →  Create a new task from the HTML form
@app.route("/add", methods=["POST"])
def add_task():
    global next_id

    # request.form holds all the <input name="..."> values
    name        = request.form.get("name",        "").strip()
    description = request.form.get("description", "").strip()
    time        = request.form.get("time",        "").strip()
    project     = request.form.get("project",     "").strip()
    group       = request.form.get("group",       "today").strip()
    priority    = request.form.get("priority",    "").strip()

    # Only save if a name was provided
    if name:
        tasks.append({
            "id":          next_id,
            "name":        name,
            "description": description,
            "time":        time,
            "project":     project,
            "group":       group,
            "priority":    priority,
            "done":        False,
        })
        next_id += 1

    # Redirect back to the home page (PRG pattern — prevents double submit)
    return redirect(url_for("index"))


# GET /toggle/<id>  →  Flip a task's done / not-done state
@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("index"))


# GET /delete/<id>  →  Remove a task permanently
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


# -------------------------------------------------------------
# START THE SERVER
# debug=True  →  auto-reloads on code change, shows error pages
# -------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)