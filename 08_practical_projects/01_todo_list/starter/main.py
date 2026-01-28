def display_menu():
    print("\n=== TO-DO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    print("==================")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else " "
            print(f"{i}. [{status}] {task["name"]}")


def add_task():
    print("add task")

def complete_task():
    print("complete task")

def delete_task():
    print("delete task")

def main():
    tasks = [
        {"name": "Clean Room", "completed": False},
        {"name": "Pray 5 times a day", "completed": True}
    ]
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Good bye")
            break
        else:
            print("\nInvalid option! Please choose 1-5.")


main()













