#Internship Task 1

 #TO DO LIST

# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' has been removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Function to display the to-do list
def display_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Goodbye!")