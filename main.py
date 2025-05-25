from abc import ABC, abstractmethod

# Abstract class for tasks
class Task(ABC):
    def __init__(self, title):
        self.title = title
        self.completed = False

    @abstractmethod
    def display(self):
        pass

    def mark_complete(self):
        self.completed = True

# Concrete class for normal task
class NormalTask(Task):
    def display(self):
        status = "✓" if self.completed else "✗"
        return f"[Normal] {status} {self.title}"

# Concrete class for priority task
class PriorityTask(Task):
    def __init__(self, title, level):
        super().__init__(title)
        self.level = level  # e.g., High, Medium, Low

    def display(self):
        status = "✓" if self.completed else "✗"
        return f"[Priority - {self.level}] {status} {self.title}"

# Task Manager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        print("\n📝 Your Tasks:")
        if not self.tasks:
            print("No tasks yet.")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task.display()}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("✅ Task marked as complete!")
        else:
            print("❌ Invalid task number.")

# CLI loop
def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Normal Task")
        print("2. Add Priority Task")
        print("3. View Tasks")
        print("4. Complete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(NormalTask(title))

        elif choice == "2":
            title = input("Enter task title: ")
            level = input("Enter priority level (High/Medium/Low): ")
            manager.add_task(PriorityTask(title, level.capitalize()))

        elif choice == "3":
            manager.show_tasks()

        elif choice == "4":
            manager.show_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                manager.complete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break

        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    main()
