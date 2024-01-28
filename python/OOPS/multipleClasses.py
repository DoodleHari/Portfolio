class Student:
    def __init__(self, name, age, grade):   # "(parameter1, parameter2)"
        self.name = name        # ".name" it's a attrubute
        self.age = age
        self.grade = grade  # = - 100

    def get_grade(self):
        return self.grade
    
# s1 = Student("Hari", 21, 99)
# print(s1.get_grde())
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Hari", 21, 99)    # s1 - object, (argument1, argument2, argument3)
s2 = Student("Leo", 21, 85)
s3 = Student("Baby", 21, 55)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.add_student(s3))
print(course.students[0].name)
print(course.get_average_grade())
