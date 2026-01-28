todo = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added!")

    elif choice == "2":
        if len(todo) == 0:
            print("No tasks available.")
        else:
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

    elif choice == "3":
        if len(todo) == 0:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number: "))
            todo.pop(num - 1)
            print("Task deleted!")

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
