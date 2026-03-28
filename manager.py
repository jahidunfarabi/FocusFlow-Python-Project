from task import Task

class TaskManager:
    """
    Manages the collection of tasks, providing methods for CRUD operations,
    sorting based on priority, and generating summary reports.
    """

    def __init__(self, initial_tasks_data):
        """
        Initializes the TaskManager with data loaded from storage.
        Converts raw dictionary data into Task objects.
        """
        # Using list comprehension for clean object conversion.
        # **data handles all keys including priority_score from JSON.
        self.tasks = [Task(**data) for data in initial_tasks_data]

    def add_task(self, title, urgency, importance):
        """
        Creates and appends a new Task object to the task list.
        Handles ID generation automatically.
        """
        # Generate a unique ID based on the last item to ensure stability[cite: 60].
        new_id = self.tasks[-1].task_id + 1 if self.tasks else 1
        
        new_task = Task(
            task_id=new_id, 
            title=title, 
            urgency=urgency, 
            importance=importance
        )
        self.tasks.append(new_task)
        return new_task

    def get_sorted_tasks(self):
        """
        Returns tasks sorted by priority score (Urgency * Importance) in descending order.
        Fulfills the 'Sort' requirement[cite: 10].
        """
        return sorted(self.tasks, key=lambda x: x.priority_score, reverse=True)

    def delete_task(self, task_id):
        """
        Removes a task by ID. Fulfills the 'Delete' part of CRUD[cite: 10].
        """
        initial_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        return len(self.tasks) < initial_length

    def search_tasks(self, query):
        """
        Searches for tasks by title (Case-insensitive). Fulfills 'Search' requirement[cite: 10].
        """
        return [t for t in self.tasks if query.lower() in t.title.lower()]

    def get_summary_report(self):
        """
        Generates statistical data. Fulfills the 'Summary Report' requirement[cite: 10, 11].
        """
        total_tasks = len(self.tasks)
        # Tasks with score 15 or higher are considered High Priority
        high_priority = len([t for t in self.tasks if t.priority_score >= 15])
        
        avg_score = 0
        if total_tasks > 0:
            avg_score = sum(t.priority_score for t in self.tasks) / total_tasks

        return {
            "total": total_tasks,
            "high_priority": high_priority,
            "average_score": round(avg_score, 2)
        }