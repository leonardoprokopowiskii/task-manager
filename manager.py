def add_task(tasks, task_name):
    task = {"name": task_name, "closed": False}
    tasks.append(task)
    print(f"\nTask '{task_name}' was added successfully!")

def view_tasks(tasks):
    print("\n-- Tasks list --")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["closed"] else " "
        task_name = task["name"]
        print(f"{index}. [{status}] - {task_name}")

def update_task(tasks, task_index, new_task_name):
    adjusted_task_index = int(task_index) - 1
    if adjusted_task_index > 0 and adjusted_task_index < len(tasks):
        tasks[adjusted_task_index]["name"] = new_task_name
        print(f"\nTask {task_index} updated to '{new_task_name}'.")
    else:
        print("\nThere is no task in the index entered!")

def close_task(tasks, task_index):
    adjusted_task_index = int(task_index) - 1
    if adjusted_task_index > 0 and adjusted_task_index < len(tasks):
        tasks[adjusted_task_index]["closed"] = True
        print(f"\nThe task {task_index} was marked as closed!")
    else:
        print("\nThere is no task in the index entered!")

tasks = []

while True:
    print("\n----- Task manager menu -----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Mark as closed task")
    print("5. Remove closed tasks")
    print("6. Exit")

    choice = input("\nType your choice: ")

    if choice == "1":
        task_name = input("Enter the name of the task: ")
        add_task(tasks, task_name)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        view_tasks(tasks)
        task_index = input("\nEnter the index of the task you want to update: ")
        new_task_name = input("Enter the new task name: ")
        update_task(tasks, task_index, new_task_name)
    elif choice == "4":
        view_tasks(tasks)
        task_index = input("\nEnter the index of the task you want mark as closed: ")
        close_task(tasks, task_index)
    elif choice == "6":
        break

print("Finish program!")
