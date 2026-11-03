import datetime
from tasks import Task, RecurringTask
from task_list import TaskList
from users import Owner


def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks.

    Args: task_list (TaskList): Task list to propagate.

    Returns: TaskList: The propagated task list.

    """
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))

    r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
    r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)

    task_list.add_task(r_task)

    return task_list


def main() -> None:
    default_owner: Owner = Owner("John", "john@example.com")
    task_list: TaskList = TaskList(default_owner)
    task_list = propagate_task_list(task_list)

    while True:
        print(f"To-Do List Manager ({task_list.owner})")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task (title / due date / description)")
        print("5. Mark a task as completed")
        print("6. View overdue tasks")
        print("7. Quit")

        choice: str = input("Enter your choice: ")

        if choice == "1":
            title: str = input("Enter a task: ")
            input_date: str = input("Enter a due date (YYYY-MM-DD): ")
            description: str = input("Enter a description (optional): ")
            date_object: datetime.datetime = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            is_recurring: str = input("Is this a recurring task? (y/n): ").strip().lower()
            if is_recurring == "y":
                interval_days: str = input("Enter the repetition interval in days: ")
                interval: datetime.timedelta = datetime.timedelta(days=int(interval_days))
                r_task: RecurringTask = RecurringTask(title, date_object, interval, description)
                task_list.add_task(r_task)
            else:
                task: Task = Task(title, date_object, description)
                task_list.add_task(task)
        elif choice == "2":
            task_list.view_tasks()
        elif choice == "3":
            ix: int = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
        elif choice == "4":
            ix = int(input("Enter the index of the task to edit: "))
            if 0 <= ix < len(task_list.tasks):
                target_task: Task = task_list.get_task(ix)
                edit_choice: str = input("Enter 1 to change title, 2 to change due date, 3 to change description: ")
                if edit_choice == "1":
                    new_title: str = input("Enter new title: ")
                    target_task.change_title(new_title)
                elif edit_choice == "2":
                    new_date_str: str = input("Enter new due date (YYYY-MM-DD): ")
                    new_date: datetime.datetime = datetime.datetime.strptime(new_date_str, "%Y-%m-%d")
                    target_task.change_date_due(new_date)
                elif edit_choice == "3":
                    new_description: str = input("Enter new description: ")
                    target_task.change_description(new_description)
                else:
                    print("Invalid edit option.")
            else:
                print("Invalid task index.")
        elif choice == "5":
            ix = int(input("Enter the index of the task to mark as completed: "))
            if 0 <= ix < len(task_list.tasks):
                task_list.get_task(ix).mark_completed()
            else:
                print("Invalid task index.")
        elif choice == "6":
            task_list.view_overdue_tasks()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
