import datetime


class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        self.title: str = title
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due

    def __str__(self) -> str:
        return (
            f"Task: {self.title} | Completed: {self.completed} | "
            f"Created: {self.date_created.strftime('%Y-%m-%d')} | "
            f"Due: {self.date_due.strftime('%Y-%m-%d')}"
        )

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def change_title(self, new_title: str) -> None:
        """Changes the title of the task.

        Args:
            new_title (str): New title for the task.
        """
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Changes the due date of the task.

        Args:
            date_due (datetime.datetime): New due date for the task.
        """
        self.date_due = date_due
