import datetime


class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime, description: str = "") -> None:
        """Creates a new task.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
            description (str): Description of the task.
        """
        self.title: str = title
        self.completed: bool = False
        self.date_created: datetime.datetime = datetime.datetime.now()
        self.date_due: datetime.datetime = date_due
        self.description: str = description

    def __str__(self) -> str:
        return (
            f"Task: {self.title} | Description: {self.description} | "
            f"Completed: {self.completed} | "
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

    def change_description(self, description: str) -> None:
        """Changes the description of the task.

        Args:
            description (str): New description for the task.
        """
        self.description = description


class RecurringTask(Task):
    """Represents a recurring task in a to-do list.

    Args:
        Task (Task): The task to be repeated.
    """

    def __init__(
        self,
        title: str,
        date_due: datetime.datetime,
        interval: datetime.timedelta,
        description: str = "",
    ) -> None:
        """Creates a new recurring task.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
            interval (datetime.timedelta): Interval between each repetition.
            description (str): Description of the task.
        """
        super().__init__(title, date_due, description)
        self.interval: datetime.timedelta = interval
        self.completed_dates: list[datetime.datetime] = []

    def _compute_next_due_date(self) -> datetime.datetime:
        """Computes the next due date of the task.

        Returns:
            datetime.datetime: The next due date of the task.
        """
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        """Marks the recurring task as completed and updates its next due date."""
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        return (
            f"{self.title} - Recurring (created: {self.date_created}, "
            f"due: {self.date_due}, completed: {self.completed_dates}, "
            f"interval: {self.interval})"
        )
