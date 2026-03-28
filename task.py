class Task:
    
    def __init__(self, task_id, title, urgency, importance, status="Pending", **kwargs):
        self.task_id = task_id
        self.title = title
        self.urgency = int(urgency)
        self.importance = int(importance)
        self.status = status
        # Score Calculation (Marks Requirement)
        self.priority_score = self.urgency * self.importance

    def to_dict(self):
        return self.__dict__