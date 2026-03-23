class Task:
    def __init__(self, task_id, title, urgency, importance, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.urgency = urgency # 1-5
        self.importance = importance # 1-5
        self.status = status
        # Priority Score = Urgency * Importance
        self.priority_score = int(urgency) * int(importance)

    def to_dict(self):
        """Convert to dictionary (for JSON saving)"""
        return self.__dict__