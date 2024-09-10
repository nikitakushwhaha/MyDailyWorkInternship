# #creataing a simple To-Do List application 
# #task name 
# #priority 
# #deadline 
# #status



# print("        TO - Do List         ")
# print("1. Add Task")
# print("2. Show Task")
# print("3. Mark Task as Done")
# print("4. Exist")
# choice = input("Enter your Choice : ")
# if choice == "1":
#     num = int(input("How many task you want to add: "))
#     for i in range(num) :
#         input("Enter the task: ")
#         print("Task added!")
# elif choice =="2":
#     print()
        

# Simple To-Do List Application in Python

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['name']} - {status}")

def add_task(tasks):
    task_name = input("\nEnter the task name: ")
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added to the list.")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("\nEnter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['name']}' removed.")
    else:
        print("Invalid task number.")

def mark_task_done(tasks):
    view_tasks(tasks)
    task_num = int(input("\nEnter the task number to mark as done: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print(f"Task '{tasks[task_num - 1]['name']}' marked as done.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            print("\nExiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
