# Task-Tracker-CLI ![Build Status](https://img.shields.io/badge/build-finished-green)


## About
Project based on 'Task Tracker CLI' challenge  by Roadmap.sh.
The challenge consists of building a CLI app to track your tasks and manage your to-do list.
To know more, visit <a href="https://roadmap.sh/projects/task-tracker"> Task Tracker CLI on Roadmap.sh </a>.

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/Ry00sh1/Task-Tracker-CLI.git
cd Task-Tracker-CLI
```

2. Set up a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install todo-cli
```

### CLI parsers

- `add <description>`: add a task with the description on <description> argument.
- `list <Optional: (todo, in-progress, done)>`: list all tasks. Optional filtering for 'status'.
- `delete <id>`: delete a task by his id.
- `mark-done <id>`: mark a task as 'done' by his id.
- `mark-in-progress <id>`: mark a task as 'in-progress' by his id.

## Example Usage

- Add a task:
```bash
todo-cli add "Go to the mall"
```

- List all tasks:
```bash
todo-cli list
```

- List all 'in-progress' tasks:
```bash
todo-cli list in-progress
```

- Mark a task as done:
```bash
todo-cli mark-done 1  # Replace 1 with the task's ID
```

- Delete task:
```bash
todo-cli delete 1  # Replace 1 with the task's ID
```

## How It Works

Tasks are stored in a JSON file (`tasks.json`), with each task having an `id`, `description`, `status`, `createdAt`, and `updatedAt` fields.
The CLI commands manipulate this file to add, remove, and update tasks.


## What did I learn with this project?
This project helped me learn how to handle JSON files in Python, including creating, updating, and reading them. It also allowed me to explore parsing CLI commands with the argparse library.
