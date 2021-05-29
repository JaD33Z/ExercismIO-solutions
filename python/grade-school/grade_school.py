
class School:
    def __init__(self):
        self.students = {}


    def add_student(self, name, grade):
        self.students[name] = grade


    def roster(self):
        kids = sorted(self.students.items(), key=lambda i: (i[1], i[0]))
        return [k for k, v in kids]


    def grade(self, grade_number):
        return sorted([attr for attr, value in self.students.items() if value == grade_number])
