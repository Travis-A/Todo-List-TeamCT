import os

# File to store tasks
FILE_NAME = "todo_list.txt"


# Load tasks from the file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []


# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


# Add a task
def add_task(task, tasks):
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    print("Task added!")


# Delete a task
def delete_task(task_index, tasks):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task index!")


# Mark a task as completed
def mark_completed(task_index, tasks):
    if 0 <= task_index < len(tasks):
        tasks[task_index] = tasks[task_index].replace("[ ]", "[x]")
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index!")


# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task}")


def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(task, tasks)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter task number to delete: ")) - 1
                delete_task(task_index, tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                mark_completed(task_index, tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
