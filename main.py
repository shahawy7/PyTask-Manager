from Task import Task
import json
import logging

logging.basicConfig(
    filename='error.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

tasks = []


def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            for item in data:
                tasks.append(Task.from_dict(item))
    except FileNotFoundError:
        with open('tasks.json', 'w') as file:
            json.dump([], file, indent=4)
    except json.JSONDecodeError as e:
        logging.error('Corrupted JSON file: %s', str(e))
        while True:
            var = input(
                'Error: tasks.json is corrupted. Would you like to delete it? [y/n]: ')
            if var == 'y':
                with open('tasks.json', 'w') as file:
                    json.dump([], file, indent=4)
                break
            elif var == 'n':
                print('Please fix the file.')
                exit()
            else:
                print('Please enter a valid answer.')
                continue


def add_task(title: str, description: str, due_date: str):
    task = Task(title, description, due_date)
    tasks.append(task)
    save_tasks()


def delete_task(task_num):
    task_id = task_num - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks()
        print(
            '==========================\nTask deleted successfully.\n==========================\n')
    else:
        logging.warning(
            f"User tried to access task #{task_num}, but it doesn't exits")
        print('\nInvalid task number.\n')


def mark_complete(task_num):
    task_id = task_num - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id].completed = True
        save_tasks()
        print('=========================\nTask marked successfully.\n=========================\n')
    else:
        logging.warning(
            f"User tried to access task #{task_num}, but it doesn't exits")
        print('\nInvalid task number.\n')


def view_tasks():
    print('=====TASKS=====')
    if not tasks:
        print('Empty')
    else:
        for id, task in enumerate(tasks):
            print(f'{id+1}: {task}')


def main():
    load_tasks()
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
                task_num = int(input('Enter task number to mark: '))
                mark_complete(task_num)
            except ValueError:
                print('\nPlease Enter a digit.\n')
        elif action == '3':
            try:
                task_num = int(input('Enter task number to delete: '))
                delete_task(task_num)
            except ValueError:
                print('\nPlease Enter a digit.\n')
        elif action == '0':
            break
        else:
            print('\nPlease provide a valid operation number.\n')
            continue


if __name__ == '__main__':
    main()
