class Task:
    def __init__(self, title: str, description: str, due_date: str, completed=False) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self) -> str:
        status = '✓' if self.completed else '✗'
        # return f'[{status}]\n{self.title} - due: {self.due_date}\nDescription: {self.description}'
        return f"[{status}] {self.title} (Due: {self.due_date})\n    {self.description}"

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(title=data['title'],
                    description=data['description'],
                    due_date=data['due_date'],
                    completed=data['completed'])
