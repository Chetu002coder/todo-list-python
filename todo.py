
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark done: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Marked '{removed}' as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n-- TO-DO LIST MENU --")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
