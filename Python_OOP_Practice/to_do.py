from datetime import date
class Task:
    todo_list = []
    def __init__(self ) -> None:
        self.name = ''
        self.description = ''
        self.deadline = None
        self.is_completed = False
        self.get_task_info()

        if Task.todo_list:
            Task.todo_list.add_task(self)

    def get_task_info(self):
        self.name = input("Enter The Name of Task: ")
        self.description = input("Enter the description for the task: ")
        self.deadline = self.set_deadline()
        if self.deadline is not None:
            print(f'Deadline date set {self.deadline}. ')

    def set_deadline(self):
        try:
            year = int(input("Enter the year of deadline: "))
            month = int(input("Enter the month of deadline: "))
            day = int(input("Enter the day of deadline: "))

            deadline_date = date(year, month, day)

            days_until_deadline = (deadline_date - date.today()).days

            if days_until_deadline > 0:
                return deadline_date
            else:
                print('Invalid Deadilne. Please set a future date.')
        except ValueError as e:
            print(f'Invalid Input: {e}')
            self.deadline = None

    def get_task_dict(self):
        task_dict = self.__dict__
        return task_dict
    

class TodoList:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task_from_Task_class):
        task_dict = task_from_Task_class.get_task_dict()
        self.tasks.append(task_dict)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, index = 1):
            print(f'Tasks {index}: {task}')

todo_list1 = TodoList()
Task.todo_list = todo_list1
task1 = Task()
task2 = Task()
task3 = Task()
todo_list1.display_tasks()
