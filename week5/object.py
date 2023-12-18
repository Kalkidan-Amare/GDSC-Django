class User:
    def __init__(self, name):
        self.name = name
class Student(User):

    list_students = []

    def __init__(self, name, age, grade):
        super().__init__(name)
        assert type(age) == int, "Age should be an integer"
        self.age = age
        self.grade = grade
        self.courses = []
        Student.list_students.append(self)

    def display(self):
        return f'Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Courses: {self.courses}'
        
    def add_course(self,course):
        self.courses.append(course)

class Course:
    def __init__(self, coursename, coursecode, teacher):
        self.coursename = coursename
        self.coursecode = coursecode
        self.teacher = teacher

    def __repr__(self):
        return f'{self.coursecode}: {self.coursename} by {self.teacher.name}'

class Teacher(User):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f'Name: {self.name} Subject: {self.subject}'

kalkidan = Student("Kalkidan", 21, 4)
kal=Student("Kal",19,3)

teshome = Teacher('Teshome', 'Math')
teshale = Teacher('Teshale', 'English')
teshnet = Teacher('Teshnet', 'Civic')

math = Course('Math', 'ma21', teshome)
english = Course('English', 'en12', teshale)
civic = Course('Civic', 'cv12', teshnet) 

kalkidan.add_course(math)
kalkidan.add_course(english)
kalkidan.add_course(civic)

print("----------------------------------------------------------------")
print(kalkidan.display())
print(math)
print(teshome)
print("----------------------------------------------------------------")
print("List of all students:\n" + "Name".ljust(15) + "Age\tGrade")
for student in Student.list_students:
    print(f'{student.name.ljust(15)}{student.age}\t{student.grade}')
print("----------------------------------------------------------------")