# todo_cli/tasks.py

import json
from datetime import datetime
from tabulate import tabulate

TASKS_FILE_PATH = './tasks.json'

def load_file() -> None:
    try:
        with open(TASKS_FILE_PATH,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_file(tasks) -> None:
    with open(TASKS_FILE_PATH, 'w') as file:
        json.dump(tasks,file,indent=4)
    
def get_next_id() -> int:
    tasks = load_file()
    ids = {task["id"] for task in tasks}
    id = 1
    while id in ids:
        id+=1
    return id

def add_task(description) -> None:
    tasks = load_file()
    id = get_next_id()

    task = {
        "id" : id,
        "description" : description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    try:
        save_file(tasks)
    except:
        return []
    finally:
        print(f"Task added successfully with id = {id}")

def list_tasks(status = None) -> None:
    tasks = load_file()
    if len(tasks) < 1:
        print("There are no tasks yet.")
        return

    if status:
        tasks = [task for task in tasks[1:] if task['status'] == status]

    headers = ["ID", "Description", "Status", "CreatedAt", "UpdatedAt"]
    rows = [[task['id'], task['description'], task['status'], task['createdAt'], task['updatedAt']]
            for task in tasks[:]]
    print(tabulate(rows, headers=headers, tablefmt="simple"))


def delete_task(task_id) -> None:
    tasks = load_file()
    tasks = [task for task in tasks if task["id"] != task_id]

    try:
        save_file(tasks)
    except:
        return []
    finally:
        print(f"Task {task_id} deleted successfully")

def mark_in_progress(task_id) -> None:
    tasks = load_file()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["status"] = "in-progress"
        task["updatedAt"] = datetime.now().isoformat()
        print("Task status is now 'in-progress'.")
        save_file(tasks)
    else:
        print(f"Task {task_id} not found.")

def mark_done(task_id) -> None:
    tasks = load_file()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["status"] = "done"
        task["updatedAt"] = datetime.now().isoformat()
        print("Task status is now 'done'.")
        save_file(tasks)
    else:
        print(f"Task {task_id} not found.")
    

