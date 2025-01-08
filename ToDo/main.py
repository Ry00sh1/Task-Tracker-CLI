import json
import os
from datetime import datetime
from tabulate import tabulate

TASKS_FILE =  os.path.join(os.path.dirname(__file__),'src', 'tasks.json')

def read_and_update_last_id(file_path):
    # Read the JSON file
    loaded_json = read_file(file_path)

    # Access the lastID
    last_id = loaded_json[0]['lastID']

    # Update the lastID
    new_last_id = last_id + 1
    loaded_json[0]['lastID'] = new_last_id

    # Write the updated JSON content back to the file
    with open(file_path, 'w') as file:
        json.dump(loaded_json, file, indent=4)

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

def update_task():
    pass
def delete_task():
    pass 

if __name__ == "__main__":
    while True:
        print("\nCRUD Operations:")
        print("1. Create task")
        print("2. Display tasks")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            id = read_and_update_last_id(TASKS_FILE)
            description = input("Descreva a tarefa: ")
            status = input("Qual o status da tarefa? (Finalizada, Em Progresso ou Concluída): ")
            createdAt = str(datetime.now())
            updatedAt = str(datetime.now())

            create_task({"id": id, "description": description, "status": status, "createdAt": createdAt, "updatedAt": updatedAt}, TASKS_FILE)
        
        elif choice == '2':
            display_tasks(TASKS_FILE)

        elif choice == '3':
            record_id = int(input("Enter ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            update_task(record_id, {"name": name, "age": age})

        elif choice == '4':
            record_id = int(input("Enter ID to delete: "))
            delete_task(record_id)

        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")