# noinspection DuplicatedCode
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
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else " "
            print(f"{i}. [{status}] {task['name']}")



def add_task(tasks):
    task_name = input("\nEnter task: ")
    tasks.append({'name': task_name, 'completed': False})
    print(f"✓ Added: {task_name}")


def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("\nEnter task number to complete: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]['completed'] = True
                print(f"✓ Completed: {tasks[num - 1]['name']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# 1 <= num <= len(tasks)

# 1- clean room => index 0
# 2- pray 5 times => index 1
# 3- Study python => index 2

# len(tasks) = 3

# 1 <= num <= 3
# User enter 2 | 1 <= 2 <=3 | True
# User enter 5 | 1 <= 5 <= 3 | False
# User enter 0 | 1 <= 0 <= 3 | False

# tasks[num - 1]['completed'] = True
# tasks[2 - 1 = 1]["completed"] = True

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(tasks):
                print(f"✓ Deleted: {tasks[num - 1]["name"]}")
                del tasks[num - 1]
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option! Please choose 1-5.")
main()