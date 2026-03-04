# task_manager.py
import json
import os

class TaskManager:
    def __init__(self):
        self.file = "data.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return {}

    def save_tasks(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, category, task, priority, due_date):
        if category not in self.tasks:
            self.tasks[category] = []

        self.tasks[category].append({
            "task": task,
            "priority": priority,
            "due": due_date,
            "status": "pending"
        })

        self.save_tasks()
        print(f'Task "{task}" added under [{category}]!')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for category, tasks in self.tasks.items():
            print(f"\n[{category}]")
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t['task']} | Status: {t['status']} | Priority: {t['priority']} | Due: {t['due']}")

    def update_task(self):
        category = input("Enter category: ")
        if category in self.tasks and self.tasks[category]:
            for i, t in enumerate(self.tasks[category]):
                print(f"{i+1}. {t['task']} | Status: {t['status']}")
            index = int(input("Select task number to mark as DONE: ")) - 1
            self.tasks[category][index]["status"] = "done"
            self.save_tasks()
            print("Task updated to DONE.")
        else:
            print("Category not found or empty.")

    def remove_task(self):
        category = input("Enter category: ")
        if category in self.tasks and self.tasks[category]:
            for i, t in enumerate(self.tasks[category]):
                print(f"{i+1}. {t['task']}")
            index = int(input("Select task number to remove: ")) - 1
            removed = self.tasks[category].pop(index)
            self.save_tasks()
            print(f'Task "{removed["task"]}" removed successfully.')
        else:
            print("Category not found or empty.")
