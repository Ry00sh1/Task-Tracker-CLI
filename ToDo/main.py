import json
import os
from datetime import datetime
from tabulate import tabulate

TASKS_FILE =  os.path.join(os.path.dirname(__file__),'src', 'tasks.json')

def search_task_by_id(file_path, task_id):
    tasks = read_file(file_path)

    # Search for the task with the given ID
    for task in tasks[1:]:
        if task.get('id') == task_id:
            return task
    return print("Task not found. Verify if the ID exists or it's correct")

def read_and_update_last_id(file_path):
    # Read the JSON file
    tasks = read_file(file_path)

    # Access the lastID
    last_id = tasks[0]['lastID']

    # Update the lastID
    new_last_id = last_id + 1
    tasks[0]['lastID'] = new_last_id

    # Write the updated JSON content back to the file
    write_task(tasks, file_path)

    return new_last_id

def read_file(file_path):
    """Read data from the JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)
    
def write_task(data, file_path):
    """Write data to the JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def create_task(task,file_path):
    """Create a new record."""
    loaded_json = read_file(file_path)
    loaded_json.append(task)
    write_task(loaded_json, file_path)
    print(f"Task created: \nDescription: {task.get('description', '')}\nStatus: {task.get('status', '')}")
    

def display_tasks(file_path):
    # Read the JSON file
    tasks = read_file(file_path)

    if len(tasks) <= 1:
        print("There are no tasks yet.")
        return

    # Extract relevant data from JSON
    headers = ["ID", "Description", "Status", "CreatedAt", "UpdatedAt"]
    rows = []
    for task in tasks[1:]:
        rows.append([task.get('id', ''), task.get('description', ''), task.get('status', ''), task.get('createdAt', ''), task.get('updatedAt', '')])

    # Display data in a tabular format
    print(tabulate(rows, headers=headers, tablefmt="simple"))

def update_task(file_path, id):
    # Read the JSON file
    tasks = read_file(file_path)

    # Find the task by id
    for task in tasks[1:]:
        if task.get('id') == id:
            print("Update...\n1. Description\n2. Status")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                input("Type the new description: ")
                new_description = input()
                updatedAt = str(datetime.now())
                task.update({'description': new_description, 'updatedAt': updatedAt})
                
            elif choice == 2:
                print("What's the new status? (todo, in-progress, done):")
                new_status = input()
                updatedAt = str(datetime.now())
                task.update({'status': new_status})
        else: 
            print("Task not found. Verify if the ID exists or if it's correct.")
            return 

 

    # Write the updated JSON content back to the file
    write_task(tasks, file_path)
    
    print("Task updated successfully.")
    

def delete_task(file_path, id):
    tasks = read_file(file_path)

    tasks = [task for task in tasks if task.get('id') != task_id]

    write_task(tasks, file_path)

if __name__ == "__main__":
    while True:
        print("\nCRUD Operations:")
        print("1. Create task")
        print("2. Display tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            id = read_and_update_last_id(TASKS_FILE)
            description = input("Describe the task: ")
            status = input("What is the status of the task? (todo, in-progress, done): ")
            createdAt = str(datetime.now())
            updatedAt = str(datetime.now())

            create_task({"id": id, "description": description, "status": status, "createdAt": createdAt, "updatedAt": updatedAt}, TASKS_FILE)
        
        elif choice == '2':
            display_tasks(TASKS_FILE)

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            update_task(TASKS_FILE,task_id)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(TASKS_FILE, task_id)

        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")