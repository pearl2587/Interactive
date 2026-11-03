class User:
    """Represents a user in the system."""

    def __init__(self, name: str, email: str) -> None:
        """Creates a new user.

        Args:
            name (str): Name of the user.
            email (str): Email address of the user.
        """
        self.name: str = name
        self.email: str = email

    def __str__(self) -> str:
        return f"User: {self.name} ({self.email})"


class Owner(User):
    """Represents an owner of a task list, inheriting from User."""

    def __init__(self, name: str, email: str) -> None:
        """Creates a new owner.

        Args:
            name (str): Name of the owner.
            email (str): Email address of the owner.
        """
        super().__init__(name, email)

    def __str__(self) -> str:
        return f"Owner: {self.name} ({self.email})"
