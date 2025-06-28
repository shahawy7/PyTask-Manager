class Task:
    def __init__(self, title: str, description: str, due_date: str) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self) -> str:
        status = '✓' if self.completed else '✗'
        # return f'[{status}]\n{self.title} - due: {self.due_date}\nDescription: {self.description}'
        return f"[{status}] {self.title} (Due: {self.due_date})\n    {self.description}"


tasks = []


def add_task(title: str, description: str, due_date: str):
    task = Task(title, description, due_date)
    tasks.append(task)


def delete_task(task_id):
    if 1 <= task_id <= len(tasks):
        tasks.pop(task_id-1)
        print('\nTask deleted successfully.\n')
    else:
        print('\nInvalid task number.\n')


def mark_complete(task_id):
    if 1 <= task_id <= len(tasks):
        tasks[task_id-1].completed = True
        print('\nTask marked successfully.\n')
    else:
        print('\nInvalid task number.\n')


def view_tasks():
    print('=====TASKS=====')
    if not tasks:
        print('Empty')
    for id, task in enumerate(tasks):
        print(f'{id+1}: {task}')


def main():

    while True:
        view_tasks()
        action = input(
            "\n[1] Add task.\n[2] Mark complete.\n[3] Delete task.\n[0] Exit.\n\nEnter operation number: ")
        if action == '1':
            while True:
                title = input('Title: ')
                description = input('Description: ')
                due_date = input('Due-date: ')
                add_task(title, description, due_date)
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
                task_id = int(input('Enter task number to mark: '))
                mark_complete(task_id)
            except ValueError:
                print('\nPlease Enter a digit.\n')
        elif action == '3':
            try:
                task_id = int(input('Enter task number to delete: '))
                delete_task(task_id)
            except ValueError:
                print('\nPlease Enter a digit.\n')
        elif action == '0':
            break
        else:
            print('\n(((Please provide a valid operation number.)))\n')
            continue


if __name__ == '__main__':
    main()
