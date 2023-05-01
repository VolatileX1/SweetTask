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
    def __init__(self, id, title, description, due_date=None, status='pending', attachments=None):
        self.id, self.title, self.description, self.status = id, title, description, status
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
        self.attachments = attachments or []
    
    def __repr__(self):
        due_date_string = f"Due Date: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else ''
        attachment_string = "\n".join([f"Attachment: {attachment}" for attachment in self.attachments])
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n{due_date_string}\n{attachment_string}\n"

def load_tasks():
    return [Task(**task) for task in json.load(open(TODO_FILE, 'r'))] if os.path.isfile(TODO_FILE) else []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def perform_action(action, args):
    if action == 'add':
        new_id = tasks[-1].id + 1 if tasks else 1
        title, description, due_date = args[:-1]
        attachments = args[-1:]
        tasks.append(Task(new_id, title, description, due_date, attachments=attachments))
        save_tasks(tasks)
        print(f"Task '{title}' added with ID {new_id}")
    elif action == 'delete':
        id = int(args[0])
        for i, task in enumerate(tasks):
            if task.id == id:
                del tasks[i]
                save_tasks(tasks)
                print(f"Task with ID {id} deleted")
                break
        else:
            print(f"No task found with ID {id}")
    elif action == 'view':
        status_filter = args[0] if args else None
        filtered_tasks = [task for task in tasks if not status_filter or task.status == status_filter]
        if filtered_tasks:
            print(*filtered_tasks, sep='\n')
        else:
            print("No tasks found")

if __name__ == '__main__':
    tasks = load_tasks()
    perform_action(args.action, args.args)
