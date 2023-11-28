class Student:
    def __init__(self):
        self.students = {}

    def add_student(self,name,age,grade):
        self.students[name] ={'age':age, 'grade':grade}
    
    def view_student(self,name):
        if name in self.students:
            student=self.students[name]
            print(f"\nName {name}\nAge {student['age']}\nGrade {student['grade']}\n")
        else:
            print(f"\nStudent {name} not found!\n")

    def list_all(self):
        for name, student in self.students.items():
            print(f"\nName {name}\nAge {student['age']}\nGrade {student['grade']}\n")

    def update_student(self,name,age=None,grade=None):
        if name in self.students:
            student=self.students[name]
            if (age != None):
                student['age'] = age
            if (grade != None):
                student['grade'] = grade
        else:
            print(f"\nStudent {name} not found!\n")

    def delete_student(self,name):
        if name in self.students:
            del self.students[name]

def main():
    stud=Student()

    while(True):
        print("\n ===============================")
        print("|    Student database Menu      |")
        print(" ===============================\n")
        print("\t1. Add Student")
        print("\t2. View Student")
        print("\t3. List All Students")
        print("\t4. Updeate Student Information")
        print("\t5. Delete Student")
        print("\t0. Exit\n")

        choice=input("Enter your choice: ")

        if choice=='1':
            name=input("Enter the student's name: ")
            age=input("Enter the age: ")
            grade=input("Enter the grade: ")
            stud.add_student(name,age,grade)
        elif choice=='2':
            name=input("Enter the student's name to search: ")
            stud.view_student(name)
        elif choice=='3':
            stud.list_all()
        elif choice=='4':
            name=input("Enter the name of the student to be changed: ")
            age=input("Enter the age: ")
            grade=input("Enter the grade: ")
            stud.update_student(name,age,grade)
        elif choice=='5':
            name=input("Enter the name of the student to be deleted: ")
            stud.delete_student(name)
        elif choice=='0':
            break
        else:
            print("Please enter a valid choice")

if __name__=='__main__':
    main()