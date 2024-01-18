class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"Student ID: {self.id}, Student Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.id}, Course Name: {self.name}"

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"Mark for student {self.student.id} in course {self.course.id}: {self.mark}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self, num_students):
        for _ in range(num_students):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.students.append(Student(id, name, dob))

    def input_courses(self, num_courses):
        for _ in range(num_courses):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.courses.append(Course(id, name))

    def input_marks(self):
        course_id = input("Enter course id to input marks: ")
        course = next((course for course in self.courses if course.id == course_id), None)
        if course is None:
            print("Invalid course id")
            return

        for student in self.students:
            mark = input(f"Enter mark for student {student.id}: ")
            self.marks.append(Mark(student, course, mark))

    def list_students(self):
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def list_marks(self):
        for mark in self.marks:
            print(mark)

def main():
    school = School()
    num_students = 0
    num_courses = 0

    while True:
        print("1. Input number of students")
        print("2. Input student info")
        print("3. Input number of courses")
        print("4. Input course info")
        print("5. Input marks for course")
        print("6. List students")
        print("7. List courses")
        print("8. List marks")
        print("9. Exit")

        option = input("Choose an option: ")

        if option == '1':
            num_students = int(input("Enter number of students: "))
        elif option == '2':
            if num_students > 0:
                school.input_students(num_students)
                num_students = 0
            else:
                print("You need to input number of students first.")
        elif option == '3':
            num_courses = int(input("Enter number of courses: "))
        elif option == '4':
            if num_courses > 0:
                school.input_courses(num_courses)
                num_courses = 0
            else:
                print("You need to input number of courses first.")
        elif option == '5':
            if len(school.students) > 0 and len(school.courses) > 0:
                school.input_marks()
            else:
                print("You need to input student and course info first.")
        elif option == '6':
            school.list_students()
        elif option == '7':
            school.list_courses()
        elif option == '8':
            school.list_marks()
        elif option == '9':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()