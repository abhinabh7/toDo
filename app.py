# =============================================================
# toDo — Flask (Python) Backend
# File: app.py
# =============================================================
# Changes from original:
#   - Replaced in-memory Python list with SQLite via Flask-SQLAlchemy
#   - Tasks now persist across container restarts
#   - All CRUD routes updated to use db.session instead of list ops
# =============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application object
app = Flask(__name__)

# -------------------------------------------------------------
# DATABASE CONFIGURATION
# SQLite file will be created at /app/instance/tasks.db inside
# the container. Mount a Docker volume to /app/instance so the
# file survives container restarts.
# -------------------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# -------------------------------------------------------------
# DATABASE MODEL
# Replaces the old Python list. Each Task is a row in the DB.
# -------------------------------------------------------------
class Task(db.Model):
    id          = db.Column(db.Integer,     primary_key=True)
    name        = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), default="")
    time        = db.Column(db.String(10),  default="")
    project     = db.Column(db.String(100), default="")
    group       = db.Column(db.String(20),  default="today")   # "today" or "upcoming"
    priority    = db.Column(db.String(10),  default="")         # "p1", "p2", or ""
    done        = db.Column(db.Boolean,     default=False)


# Create tables if they don't exist yet (runs once on startup)
with app.app_context():
    db.create_all()

    # Seed some starter tasks only if the table is empty
    if Task.query.count() == 0:
        seed_tasks = [
            Task(name="Do 30 minutes of yoga 🧘", time="07:30", project="Health",    group="today",    priority="p1"),
            Task(name="Dentist appointment",       time="10:00", project="Personal",  group="today"),
            Task(name="Buy bread 🍞",              description="Sourdough loaf",      project="Shopping", group="today"),
            Task(name="Team standup meeting",      time="09:00", project="Work",      group="upcoming", priority="p2"),
            Task(name="Review project proposal",   time="14:00", project="Work",      group="upcoming", priority="p1"),
        ]
        db.session.add_all(seed_tasks)
        db.session.commit()


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
    """Convert 24-hour string 'HH:MM' → 12-hour string '7:30 AM'."""
    if not t:
        return ""
    h, m = map(int, t.split(":"))
    ampm = "AM" if h < 12 else "PM"
    h12  = h % 12 or 12
    return f"{h12}:{m:02d} {ampm}"


# -------------------------------------------------------------
# ROUTES
# -------------------------------------------------------------

# GET / → Home page
@app.route("/")
def index():
    active_view = request.args.get("view", "today")
    if active_view not in ("today", "upcoming"):
        active_view = "today"

    today    = Task.query.filter_by(group="today").all()
    upcoming = Task.query.filter_by(group="upcoming").all()

    return render_template(
        "index.html",
        today=today,
        upcoming=upcoming,
        active_view=active_view,
        project_colors=PROJECT_COLORS,
        all_projects=list(PROJECT_COLORS.keys()),
        format_time=format_time,
    )


# POST /add → Create a new task
@app.route("/add", methods=["POST"])
def add_task():
    name = request.form.get("name", "").strip()
    if name:
        task = Task(
            name        = name,
            description = request.form.get("description", "").strip(),
            time        = request.form.get("time", "").strip(),
            project     = request.form.get("project", "").strip(),
            group       = request.form.get("group", "today").strip(),
            priority    = request.form.get("priority", "").strip(),
        )
        db.session.add(task)
        db.session.commit()

    # PRG pattern — prevents double-submit on browser refresh
    return redirect(url_for("index"))


# GET /toggle/<id> → Flip done / not-done
@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("index"))


# GET /delete/<id> → Remove a task permanently
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))


# -------------------------------------------------------------
# START THE SERVER
# debug=False in production — use gunicorn via docker-compose
# Keep debug=True only for local development outside Docker
# -------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)