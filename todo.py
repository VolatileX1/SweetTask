import argparse
import json

# Define the command-line arguments using argparse
parser = argparse.ArgumentParser(description='Manage your daily tasks efficiently')
group = parser.add_mutually_exclusive_group()
group.add_argument('--status', choices=['completed', 'pending', 'due'], help='Filter tasks by status')
parser.add_argument('action', choices=['add', 'delete', 'view'], help='Action to perform')
parser.add_argument('args', nargs='*', help='Action arguments')

# Define the path to the JSON file where tasks will be stored
TODO_FILE = 'todo.json'

class Task:
    """Class representing a single task"""
    def __init__(self, id, title, description, status='pending'):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
    
    def __repr__(self):
        """Return a string representation of a task"""
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n"

def load_tasks():
    """Load tasks from the JSON file"""
    try:
        with open(TODO_FILE, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return [Task(**task) for task in tasks]

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TODO_FILE, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def add_task(args):
    """Add a new task"""
    # Generate a new ID for the task
    if len(tasks) > 0:
        new_id = tasks[-1].id + 1
    else:
        new_id = 1
    
    # Create a new task object and append it to the list
    title, description = args
    tasks.append(Task(new_id, title, description))
    save_tasks(tasks)
    print(f"Task '{title}' added with ID {new_id}")

def delete_task(args):
    """Delete an existing task"""
    id = int(args[0])
    
    # Find the task by ID and remove it from the list
    for i, task in enumerate(tasks):
        if task.id == id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task with ID {id} deleted")
            break
    else:
        print(f"No task found with ID {id}")

def view_tasks(args):
    """View all tasks"""
    status_filter = args[0] if len(args) > 0 else None
    
    # Filter tasks by status if specified
    if status_filter:
        filtered_tasks = [task for task in tasks if task.status == status_filter]
    else:
        filtered_tasks = tasks
    
    # Print out all the tasks
    if len(filtered_tasks) > 0:
        for task in filtered_tasks:
            print(task)
    else:
        print("No tasks found")

if __name__ == '__main__':
    tasks = load_tasks()
    
    # Parse the command-line arguments and call the appropriate function
    args = parser.parse_args()
    action = args.action
    func = {
        'add': add_task,
        'delete': delete_task,
        'view': view_tasks
    }[action]
    func(args.args)
