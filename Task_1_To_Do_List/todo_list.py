tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\n--- YOUR TASKS ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Your task list is empty. Add a task first.")
        else:
            print("\n--- YOUR TASKS ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter task number to update: "))

                if 1 <= task_number <= len(tasks):
                    new_task = input("Enter new task: ")

                    if new_task.strip() == "":
                        print("Task cannot be empty.")
                    else:
                        tasks[task_number - 1] = new_task
                        print(f"Task '{new_task}' updated successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter numbers only.")

    elif choice == "4":
        if len(tasks) == 0:
            print("Your task list is empty. Nothing to delete.")
        else:
            print("\n--- YOUR TASKS ---")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Task deleted successfully: {deleted_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter numbers only.")

    elif choice == "5":
        print("Thank you! Program closed.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
