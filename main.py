from TaskManager import TaskManager


def main():
    manager = TaskManager()

    while True:
        manager.view_tasks()
        action = input(
            "\n[1] Add task.\n[2] Mark complete.\n[3] Delete task.\n[0] Exit.\n\nEnter operation number: ")
        if action == '1':
            while True:
                title = input('Title: ')
                description = input('Description: ')
                due_date = input('Due-date: ')
                manager.add_task(title, description, due_date)
                while True:
                    add_another = input('Add another task? [y/n]: ')
                    if add_another == 'y':
                        break
                    elif add_another == 'n':
                        break
                    else:
                        print('Please input a valid answer.')
                        continue
                if add_another == 'n':
                    break

        elif action == '2':
            try:
                task_num = int(input('Enter task number to mark: '))
                manager.mark_complete(task_num)
            except ValueError:
                print('\nPlease Enter a digit.\n')
        elif action == '3':
            try:
                task_num = int(input('Enter task number to delete: '))
                manager.delete_task(task_num)
            except ValueError:
                print('\nPlease Enter a digit.\n')
        elif action == '0':
            break
        else:
            print('\nPlease provide a valid operation number.\n')
            continue


if __name__ == '__main__':
    main()
