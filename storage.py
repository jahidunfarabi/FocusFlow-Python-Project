import json
import os

class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks_list):
        """All task save into JSON file"""
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks_list], f, indent=4)

    def load_tasks(self):
        """File to data as a list"""
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)