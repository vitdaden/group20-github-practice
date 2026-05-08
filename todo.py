class Todo:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def mark_undone(self):
        self.completed = False

    def __str__(self):
        status = "✅" if self.completed else "⬜"
        desc = f" - {self.description}" if self.description else ""
        return f"[{self.id}] {status} {self.title}{desc}"
