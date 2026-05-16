import json
import os
from typing import List
from task import Task

class TaskScheduler:
    """Handles data processing, sorting algorithms, and file I/O."""
    
    def __init__(self, storage_path: str = "data/tasks.json"):
        self.storage_path = storage_path
        self._tasks: List[Task] = self._load_data()

    def _load_data(self) -> List[Task]:
        """Loads data from JSON with error handling for corrupted files."""
        if not os.path.exists(self.storage_path):
            return []
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_data(self):
        """Persists the current task list to disk."""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self._tasks], f, indent=4)

    def add_task(self, title: str, priority: int, deadline: str):
        """Adds a task and triggers the sorting algorithm."""
        new_task = Task(title, priority, deadline)
        self._tasks.append(new_task)
        self._sort_tasks()  # Maintains order
        self.save_data()

    def _sort_tasks(self):
        """
        ALGORITHM: Multi-level Priority Sort.
        Complexity: O(N log N) using Python's Timsort.
        Sorts by Priority (Ascending) then Title (Alphabetical).
        """
        self._tasks.sort(key=lambda x: (x.priority, x.title.lower()))

    def delete_task(self, index: int) -> bool:
        """Removes a task by index with bounds checking."""
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)
            self.save_data()
            return True
        return False

    def get_all_tasks(self) -> List[Task]:
        return self._tasks