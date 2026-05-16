"""
Module defining the Task entity for the EliteTask Scheduler.
"""

class Task:
    """
    Represents a single task with priority and deadline.
    
    Attributes:
        title (str): The name of the task.
        priority (int): Importance scale 1-5 (1 being highest).
        deadline (str): Date string (YYYY-MM-DD).
    """
    def __init__(self, title: str, priority: int, deadline: str):
        self.title = title
        self.priority = priority
        self.deadline = deadline

    def to_dict(self) -> dict:
        """Converts object to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline
        }

    def __str__(self) -> str:
        return f"[{self.priority}] {self.title} (Due: {self.deadline})"