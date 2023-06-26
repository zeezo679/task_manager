tasks = []

def menu():
    #task menu
    print("To-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")



def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added!")


def view_tasks():
    if len(tasks) > 0:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    else:
        print("No tasks found!")
    

def completed_task():
    print("Tasks: ")
    view_tasks()
    taskNum = input("Enter the task number to mark as completed: ")
    print(f"Marked task '{tasks[int(taskNum) - 1]}' as completed.")
    del tasks[int(taskNum)-1]

def delete_task():
    print("Tasks: ")
    view_tasks()
    taskNum = int(input("Enter the task number to be deleted: "))
    print(f"Deleted '{tasks[int(taskNum) - 1]}'")
    del tasks[int(taskNum)-1]


while True:
    menu()
    choice = input("Enter you choice (1-5): ")

    if choice == "1":
        add_task()
        print("=" * 10)
    elif choice == "2":
        view_tasks()
        print("="*10)
    elif choice == "3":
        completed_task()
        print("="*10)
    elif choice == "4":
        delete_task()
        print("="*10)
    elif choice == "5":
        print("Exiting...")
        break