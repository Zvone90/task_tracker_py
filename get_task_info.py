import json

class Get_task_info:
    def __init__(self, data):
        self.data = data
        # self.task_id = task_id
    
    def print_data_info(self):
        data = json.load(self.data)
        print(json.dumps(data, indent=4))
        
    def get_task_by_id(self, task_id):
        data = json.load(self.data)
        for task in data["content"]:
            if task["id"] == task_id:
                return task
        return None
    
    def get_task_by_status(self, status_type):
        data = json.load(self.data)
        matches = []
        for task in data["content"]:
            if status_type.lower() in task["Status"].lower():
                matches.append(task)
        return matches
    

    def update_task_status(self, task_id, new_status):
        self.data.seek(0)
        data = json.load(self.data)
        for task in data["content"]:
            if task["id"] == task_id:
                data["Status"] = new_status
                break
    
        with open("task_list.json", "w") as file:
            json.dump(data, file, indent=4)
        return task