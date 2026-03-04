# main.py
from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n—— TaskMaster ——")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category: ")
            task = input("Enter task: ")
            priority = input("Enter priority (Low/Medium/High): ")
            due_date = input("Enter due date (optional): ")
            manager.add_task(category, task, priority, due_date)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.update_task()

        elif choice == "4":
            manager.remove_task()

        elif choice == "5":
            print("Program exited.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
