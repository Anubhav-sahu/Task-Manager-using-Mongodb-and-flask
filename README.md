# Task-Manager-using-Mongodb-and-flask

# Task Manager-
A simple Task Manager web application built with Flask and MongoDB Atlas. It allows users to add, edit, delete, and view tasks with an intuitive UI.

## Features
- Add new tasks with a name and description.
- Edit existing tasks, including marking them as completed.
- Delete tasks.
- View all tasks in a visually appealing card layout.

---

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.7 or later
- MongoDB Atlas account (or access to a MongoDB instance)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install Flask pymongo dnspython
   ```

4. Set up MongoDB Atlas:
   - Create a cluster in [MongoDB Atlas](https://www.mongodb.com/atlas/database).
   - Get the connection string for your cluster.
   - Replace `<username>` and `<password>` in the connection string in `app.py` with your MongoDB credentials.

---

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the app to manage tasks.

---

## File Structure
```
task_manager/
│
├── app.py                # Main application file
├── requirements.txt      # List of dependencies
├── static/
│   └── css/
│       └── styles.css    # Custom CSS styles
├── templates/
│   ├── index.html        # Home page template
│   ├── add_task.html     # Add task page template
│   └── edit_task.html    # Edit task page template
└── README.md             # Project documentation
```

---

---

## Contributing
Feel free to submit pull requests or open issues to improve this project!

