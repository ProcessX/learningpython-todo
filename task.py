class Task:

    title = "Task"
    done = False

    def __init__(self, title):
        self.title = title

    def check(self):
        self.done = not self.done