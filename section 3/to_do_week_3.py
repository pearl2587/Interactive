tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        for index in range(len(tasks)):
            print(f"{index + 1}. {tasks[index]}")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' does not exist in the list.")


while True:
    print("To-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter the task to add: ")
        add_task(new_task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_to_remove = input("Enter the task to remove: ")
        remove_task(task_to_remove)
    elif choice == "4":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
