import sys
from scheduler import TaskScheduler

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    """Robust input validation to prevent CLI crashes."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main_menu():
    engine = TaskScheduler()
    
    while True:
        print("\n--- ELITETASK: CLI PRIORITY SCHEDULER ---")
        print("1. View Sorted Tasks")
        print("2. Add New Task")
        print("3. Remove Task (Complete)")
        print("4. Exit")
        
        choice = input("\nSelect Option: ")

        if choice == '1':
            tasks = engine.get_all_tasks()
            if not tasks:
                print("\n[!] No tasks pending.")
            else:
                print("\nCURRENT TASKS (Sorted by Priority):")
                for i, t in enumerate(tasks):
                    print(f"{i}. {t}")

        elif choice == '2':
            title = input("Enter Task Name: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            priority = get_valid_int("Enter Priority (1-High, 5-Low): ", 1, 5)
            deadline = input("Enter Deadline (YYYY-MM-DD): ")
            engine.add_task(title, priority, deadline)
            print("✔ Task recorded.")

        elif choice == '3':
            tasks = engine.get_all_tasks()
            if not tasks:
                print("Nothing to delete.")
                continue
            idx = get_valid_int("Enter Task Index to remove: ", 0, len(tasks)-1)
            if engine.delete_task(idx):
                print("✔ Task removed.")

        elif choice == '4':
            print("Closing Scheduler. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main_menu()