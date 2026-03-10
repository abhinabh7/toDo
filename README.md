# toDo — Task Manager App (Flask Version)

A clean and simple **Task Manager web application built with Python and Flask**.

This project allows users to create, organize, and manage tasks using a modern sidebar interface similar to popular productivity apps.

The application is designed for **learning web development and DevOps fundamentals** with a simple backend and clean UI.

---

## Features

- Full-screen responsive layout
- Sidebar navigation with **Today** and **Upcoming** views
- Tasks grouped by **Projects**
- Color-coded project indicators
- Add tasks with:
  - Name
  - Description
  - Time
  - Priority
  - Project
  - Group
- Mark tasks **completed**
- Delete tasks
- Mobile-friendly interface

---

## Project Structure

```
todo-app-flask/
│
├── app.py
│   Main Flask application
│   Contains routes, task logic, and helper functions
│
├── requirements.txt
│   Python dependencies
│
├── templates/
│   └── index.html
│       HTML template rendered by Flask
│
└── static/
    └── css/
        └── style.css
        Application styles
```

---

## Requirements

- Python **3.8 or higher**
- pip (Python package manager)

---

## Installation and Setup

### 1. Check Python installation

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed, download it from:

https://www.python.org

---

### 2. Clone the repository

```bash
git clone <your-repository-url>
cd todo-app-flask
```

Or open the project folder manually.

---

### 3. Create a Virtual Environment

A virtual environment keeps project dependencies separate from system packages.

```bash
python -m venv venv
```

#### Activate the environment

Windows:

```bash
venv\Scripts\activate
```

Mac / Linux:

```bash
source venv/bin/activate
```

When activated, your terminal will show:

```
(venv)
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

This installs:

- Flask

---

### 5. Run the application

```bash
python app.py
```

You should see:

```
* Running on http://127.0.0.1:5000
```

---

### 6. Open the application

Open your browser and go to:

```
http://localhost:5000
```

---

## Stop the Server

Press:

```
CTRL + C
```

in the terminal.

---

## Deactivate Virtual Environment

```bash
deactivate
```

---

## Application Routes

| Method | Route | Description |
|------|------|------|
| GET | `/` | Display the main task page |
| GET | `/?view=upcoming` | Show upcoming tasks |
| POST | `/add` | Add a new task |
| GET | `/toggle/<id>` | Mark task done / undone |
| GET | `/delete/<id>` | Delete a task |

---

## Task Data Model

Each task contains the following fields:

| Field | Type | Example |
|------|------|------|
| id | integer | 1 |
| name | string | Buy groceries |
| description | string | Milk and bread |
| time | string | 07:30 |
| project | string | Shopping |
| group | string | today |
| priority | string | p1, p2, p3 |
| done | boolean | true / false |

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2 Templates

---

## Future Improvements

Possible features to extend the project:

- Store tasks using **SQLite database**
- Add **task editing**
- Add **due dates**
- Implement **user authentication**
- Add **dark mode**
- Build a **REST API**

---

## Purpose of the Project

This project was built for:

- Learning **Flask web development**
- Understanding **backend routing**
- Practicing **template rendering**
- Preparing for **DevOps deployment projects**

---

## License

This project is open-source and available for learning purposes.
