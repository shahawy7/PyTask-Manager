class Task:
    def __init__(self, title: str, description: str, due_date: str) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self) -> str:
        status = '✓' if self.completed else '✗'
        return f'[{status}] {self.title} - due: {self.due_date}\n    Description: {self.description}'


def main():
    task = Task("Buy groceries", "Milk, Eggs, Bread", "2025-06-23")
    print(task)


if __name__ == '__main__':
    main()
