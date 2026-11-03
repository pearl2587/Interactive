import datetime
from tasks import Task


class TaskList:
    """Represents a collection of tasks in a to-do list."""

    def __init__(self, owner: str) -> None:
        self.owner: str = owner.upper()
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a task to the task list.

        Args:
            task (Task): The task object to add.
        """
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        """Removes a task from the task list by index.

        Args:
            ix (int): Index of the task to remove.
        """
        if 0 <= ix < len(self.tasks):
            del self.tasks[ix]
        else:
            print("Invalid task index.")

    def get_task(self, ix: int) -> Task:
        """Returns the task at the specified index.

        Args:
            ix (int): Index of the task to retrieve.

        Returns:
            Task: The task at the given index.
        """
        return self.tasks[ix]

    def view_tasks(self) -> None:
        """Prints all tasks in the task list with their indices."""
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

    def view_overdue_tasks(self) -> None:
        """Prints all overdue tasks in the task list based on the current date."""
        now: datetime.datetime = datetime.datetime.now()
        for index, task in enumerate(self.tasks):
            if task.date_due < now and not task.completed:
                print(f"{index}: {task}")
