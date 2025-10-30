# ===============================
# Simple To-Do List Application
# Author: Mohamed Elkashef
# Description:
#   A simple command-line To-Do List app that allows
#   the user to add, delete, and mark tasks as done.
# ===============================

tasks = []

def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter new task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Task '{title}' added successfully!")
    else:
        print("Task title cannot be empty!")

def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Task '{removed['title']}' deleted.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def mark_done():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print(f"Task '{tasks[index]['title']}' marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
