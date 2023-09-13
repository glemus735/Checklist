import os

# Function to display the task list
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. Title: {task['title']}, Description: {task['description']}, Status: {status}")

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description, "completed": False})
    print("Task added successfully!")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    choice = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    choice = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= choice < len(tasks):
        del tasks[choice]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = []  # List to store tasks

    while True:
        print("\nTask List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")
       
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
