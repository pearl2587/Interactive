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

    def view_tasks(self) -> None:
        """Prints all tasks in the task list with their indices."""
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")
