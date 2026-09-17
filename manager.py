def add_task(tasks, task_name):
    task = {"name": task_name, "closed": False}
    tasks.append(task)
    print(f"\nTask '{task_name}' was added successfully!")

tasks = []

while True:
    print("\n----- Task manager menu -----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Closed task")
    print("5. Remove closed tasks")
    print("6. Exit")

    choice = input("\nType your choice: ")

    if choice == "1":
        task_name = input("Enter the name of the task: ")
        add_task(tasks, task_name)
    elif choice == "6":
        break

print("Finish program!")
