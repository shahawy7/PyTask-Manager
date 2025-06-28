from Task import Task
import logging
import json
logging.basicConfig(
    filename='error.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class TaskManager():
    def __init__(self) -> None:
        self.tasks = []
        self.filename = 'tasks.json'
        self.load_tasks()

    def add_task(self, title: str, description: str, due_date: str):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_num):
        task_id = task_num - 1
        if 0 <= task_id < len(self.tasks):
            self.tasks.pop(task_id)
            self.save_tasks()
            print(
                '==========================\nTask deleted successfully.\n==========================\n')
        else:
            logging.warning(
                f"User tried to access task #{task_num}, but it doesn't exits")
            print('\nInvalid task number.\n')

    def mark_complete(self, task_num):
        task_id = task_num - 1
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].completed = True
            self.save_tasks()
            print(
                '=========================\nTask marked successfully.\n=========================\n')
        else:
            logging.warning(
                f"User tried to access task #{task_num}, but it doesn't exits")
            print('\nInvalid task number.\n')

    def view_tasks(self):
        print('=====TASKS=====')
        if not self.tasks:
            print('Empty')
        else:
            for id, task in enumerate(self.tasks):
                print(f'{id+1}: {task}')

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.tasks.append(Task.from_dict(item))
        except FileNotFoundError:
            with open(self.filename, 'w') as file:
                json.dump([], file, indent=4)
        except json.JSONDecodeError as e:
            logging.error('Corrupted JSON file: %s', str(e))
            while True:
                var = input(
                    'Error: tasks.json is corrupted. Would you like to delete it? [y/n]: ')
                if var == 'y':
                    with open(self.filename, 'w') as file:
                        json.dump([], file, indent=4)
                    break
                elif var == 'n':
                    print('Please fix the file.')
                    exit()
                else:
                    print('Please enter a valid answer.')
                    continue
