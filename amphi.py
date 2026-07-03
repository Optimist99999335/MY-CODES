Task = []
def start():
    print('-' * 45)
    print("       Welcome to Korede's To-Do App")
    print('-' * 45)

    while True:
        print('\nSelect Operation')
        print("1. Add Task(s)")
        print("2. View Task(s)")
        print("3. Delete Task(s)")
        print("4. Exit")

        choice = input("What do you want to do? ").strip()

        if choice == '4':
            print("To-Do App is closed!")
            break

        elif choice == '1':
            new_task = input("What Task do you want to add? ").strip()
            Task.append(new_task)
            print("Task Added")
            continue

        elif choice == '2':
            if len(Task) == 0:
                print("No task available!")
                continue

            else:
                for i in range(len(Task)):
                    if 1 >= i <= len(Task):
                        print(i + 1, '-', Task[i])
                        continue
        
        elif choice == '3':
            if len(Task) == 0:
                print("No task available!")
                continue

            else:
                for i in range(len(Task)):
                    if 1 >= i <= len(Task):
                        print(i + 1, '-', Task[i])
                        continue
            
            try:    
                number = input("What task(number) do you want to delete? ").strip()
                number = int(number)

            except ValueError:
                print('Enter a Valid whole number')
                continue

            if 1 <= number and number <= len(Task):
                removed = number - 1
                Task[removed].remove()
                print('Task Deleted!')
                continue
            else:
                print('Error! out of bounds')

                
            
start()