import math
import curses
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = []

    def __str__(self):
        return f"Student ID: {self.id}, Student Name: {self.name}, DoB: {self.dob}"

    def calculate_gpa(self):
        total_marks = np.array([mark.mark for mark in self.marks])
        total_credits = np.array([mark.course.credit for mark in self.marks])
        return np.sum(total_marks * total_credits) / np.sum(total_credits)

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Course ID: {self.id}, Course Name: {self.name}, Credit: {self.credit}"
    
class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"Mark for student {self.student.id} in course {self.course.id}: {self.mark}"

class School:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self, num_students):
        for _ in range(num_students):
            self.stdscr.addstr("================================================\n")
            self.stdscr.addstr("Enter student id: ")
            id = self.stdscr.getstr().decode('utf-8')
            self.stdscr.addstr("Enter student name: ")
            name = self.stdscr.getstr().decode('utf-8')
            self.stdscr.addstr("Enter student DoB: ")
            dob = self.stdscr.getstr().decode('utf-8')
            self.students.append(Student(id, name, dob))

    def input_courses(self, num_courses):
        for _ in range(num_courses):
            self.stdscr.addstr("================================================\n")
            self.stdscr.addstr("Enter course id: ")
            id = self.stdscr.getstr().decode('utf-8')
            self.stdscr.addstr("Enter course name: ")
            name = self.stdscr.getstr().decode('utf-8')
            self.stdscr.addstr("Enter course credit: ")
            credit = int(self.stdscr.getstr().decode('utf-8'))
            self.courses.append(Course(id, name, credit))

    def input_marks(self):
        self.stdscr.addstr("================================================\n")
        self.stdscr.addstr("Enter course id to input marks: ")
        course_id = self.stdscr.getstr().decode('utf-8')
        course = next((course for course in self.courses if course.id == course_id), None)
        if course is None:
            self.stdscr.addstr("Invalid course id\n")
            return

        for student in self.students:
            self.stdscr.addstr(f"Enter mark for student {student.id}: ")
            mark = float(self.stdscr.getstr().decode('utf-8'))
            mark = math.floor(mark * 10) / 10  # round down to 1 decimal place
            mark_obj = Mark(student, course, mark)
            self.marks.append(mark_obj)
            student.marks.append(mark_obj)  # add mark to student's marks

    def list_students(self):
        if len(self.students) == 0:
            self.stdscr.addstr("No students to list. Input student info first.\n")
            return
        for student in self.students:
            self.stdscr.addstr(str(student) + "\n")

    def list_courses(self):
        if len(self.courses) == 0:
            self.stdscr.addstr("No courses to list. Input course info first.\n")
            return
        for course in self.courses:
            self.stdscr.addstr(str(course) + "\n")

    def list_marks(self):
        if len(self.marks) == 0:
            self.stdscr.addstr("No marks to list. Input marks for course first.\n")
            return
        for mark in self.marks:
            self.stdscr.addstr(str(mark) + "\n")

    def sort_students_by_gpa(self):
        self.students = sorted(self.students, key=lambda student: student.calculate_gpa(), reverse=True)
        for student in self.students:
            self.stdscr.addstr(f"{student} GPA: {student.calculate_gpa()}\n")

def main(stdscr):
    school = School(stdscr)
    num_students = 0
    num_courses = 0

    while True:
        stdscr.addstr("================================================\n")
        stdscr.addstr("1. Input number of students\n")
        stdscr.addstr("2. Input student info\n")
        stdscr.addstr("3. Input number of courses\n")
        stdscr.addstr("4. Input course info\n")
        stdscr.addstr("5. Input marks for course\n")
        stdscr.addstr("6. List students\n")
        stdscr.addstr("7. List courses\n")
        stdscr.addstr("8. List marks\n")
        stdscr.addstr("9. Sort students by GPA\n")
        stdscr.addstr("10. Exit\n")

        stdscr.addstr("Choose an option: ")
        option = stdscr.getstr().decode('utf-8')

        if option == '1':
            stdscr.addstr("Enter number of students: ")
            num_students = int(stdscr.getstr().decode('utf-8'))
        elif option == '2':
            if num_students > 0:
                school.input_students(num_students)
                num_students = 0
            else:
                stdscr.addstr("You need to input number of students first.\n")
        elif option == '3':
            stdscr.addstr("Enter number of courses: ")
            num_courses = int(stdscr.getstr().decode('utf-8'))
        elif option == '4':
            if num_courses > 0:
                school.input_courses(num_courses)
                num_courses = 0
            else:
                stdscr.addstr("You need to input number of courses first.\n")
        elif option == '5':
            if len(school.students) > 0 and len(school.courses) > 0:
                school.input_marks()
            else:
                stdscr.addstr("You need to input student and course info first.\n")
        elif option == '6':
            school.list_students()
        elif option == '7':
            school.list_courses()
        elif option == '8':
            school.list_marks()
        elif option == '9':
            school.sort_students_by_gpa()
        elif option == '10':
            break
        else:
            stdscr.addstr("Invalid option. Please try again.\n")

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)