import numpy as np
class Student:
    # subjects = ['Math', 'Science', 'History']
    
    def __init__(self, name, age, grades = None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []


    def counts(self):
        self.count = int(input(f"Enter the Number of Subjects for {self.name}: "))
        return self.count
    

    def add_grades(self):
        
        for i in range(self.counts()):
            grade = float(input(f"Enter Grade for Subject {i + 1} for {self.name} : "))
            self.grades.append(grade)
        return self.grades

    def calculate_average(self):
        return np.mean(self.grades)


student1 = Student('Sukh', 23)
student2 = Student('Noor', 23)

student1.add_grades()
print(f'Average Marks for {student1.name}: {student1.calculate_average()}')


student2.add_grades()
print(f'Average Marks for {student2.name}: {student2.calculate_average()}')