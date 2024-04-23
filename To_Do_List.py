class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def update_task(self, index, task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = task
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task.description}")
        else:
            print("Your to-do list is empty.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter index of task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            index = int(input("Enter index of task to update: ")) - 1
            description = input("Enter new description: ")
            due_date = input("Enter new due date (optional): ")
            priority = input("Enter new priority (optional): ")
            task = Task(description, due_date, priority)
            todo_list.update_task(index, task)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
