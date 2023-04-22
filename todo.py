import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser(description='Manage your daily tasks efficiently')
group = parser.add_mutually_exclusive_group()
group.add_argument('--status', choices=['completed', 'pending', 'due'], help='Filter tasks by status')
parser.add_argument('action', choices=['add', 'delete', 'view'], help='Action to perform')
parser.add_argument('args', nargs='*', help='Action arguments')

TODO_FILE = 'todo.json'

class Task:
    def __init__(self, id, title, description, due_date=None, status='pending'):
        self.id, self.title, self.description, self.status = id, title, description, status
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
    
    def __repr__(self):
        due_date_string = f"Due Date: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else ''
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n{due_date_string}\n"

def load_tasks():
    try:
        with open(TODO_FILE, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return [Task(**task) for task in tasks]

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def add_task(args):
    new_id = tasks[-1].id + 1 if tasks else 1
    title, description, due_date = args
    tasks.append(Task(new_id, title, description, due_date))
    save_tasks(tasks)
    print(f"Task '{title}' added with ID {new_id}")

def delete_task(args):
    id = int(args[0])
    for i, task in enumerate(tasks):
        if task.id == id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task with ID {id} deleted")
            break
    else:
        print(f"No task found with ID {id}")

def view_tasks(args):
    status_filter = args[0] if args else None
    filtered_tasks = [task for task in tasks if not status_filter or task.status == status_filter]
    if filtered_tasks:
        print(*filtered_tasks, sep='\n')
    else:
        print("No tasks found")

if __name__ == '__main__':
    tasks = load_tasks()
    action_func = {'add': add_task, 'delete': delete_task, 'view': view_tasks}[args.action]
    action_func(args.args)
