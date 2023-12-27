
tasks = []
def display_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid index. Please enter a valid task number.")
while True:
    print("\nTo-Do List Menu:")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_tasks()

    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)

    elif choice == '3':
        display_tasks()
        index = input("Enter the task number to remove: ")
        try:
            index = int(index)
            remove_task(index)
        except ValueError:
            print("Please enter a valid task number.")

    elif choice == '4':
        print("To-Do List exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
