
class Action():
    def __init__(self, action) -> None:
        self.action = action
    
    def execute(self):
        self.action()

    