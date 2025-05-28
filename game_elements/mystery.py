
class Mystery:
    def __init__(self, name: str, status = False):
        self.name = name
        self.status = status

    def check_status(self):
        return self.status

    def set_as_completed(self):
        self.status = True

    def set_status(self, new_status):
        self.status = new_status
