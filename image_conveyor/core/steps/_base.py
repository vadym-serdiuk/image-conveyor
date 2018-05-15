class Step():
    task = None

    def __init__(self, task):
        self.task = task

    def finished(self):
        self.task.run_next_step()

    def run(self):
        pass