import json

class Add_task:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status

    def update_task(self, id, new_description):
        self.id = id
        self.description = new_description

    def update_task_status(self, id, new_status):
        self.id = id
        self.status = new_status

    def get_task_info(self):
        print(f"Task #: {self.id}\nDescription: {self.description}\nStatus: {self.status}")
    
    
    