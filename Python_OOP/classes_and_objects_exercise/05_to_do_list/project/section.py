from typing import List
from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_Task: Task):
        if new_Task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_Task)
        return f"Task {new_Task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks_counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_tasks_counter += 1

        return f"Cleared {removed_tasks_counter} tasks."

    def view_section(self):
        result = []
        result.append(f"Section {self.name}:")
        [result.append(task.details()) for task in self.tasks]

        return '\n'.join(result)


section = Section("New section")
print(section.view_section().strip())



