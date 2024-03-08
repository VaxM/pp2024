import os
import pickle
import gzip
import curses
import threading
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import input
import output

def save_data(students, courses, marks):
    with gzip.open('students.dat', 'wb') as f:
        pickle.dump((students, courses, marks), f)

def main(stdscr):
    num_students = 0
    num_courses = 0
    students = []
    courses = []
    marks = []
    if os.path.exists('students.dat'):
        with gzip.open('students.dat', 'rb') as f:
            students, courses, marks = pickle.load(f)

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
                students = input.input_students(stdscr, num_students)
                num_students = 0
            else:
                stdscr.addstr("You need to input number of students first.\n")
        elif option == '3':
            stdscr.addstr("Enter number of courses: ")
            num_courses = int(stdscr.getstr().decode('utf-8'))
        elif option == '4':
            if num_courses > 0:
                courses = input.input_courses(stdscr, num_courses)
                num_courses = 0
            else:
                stdscr.addstr("You need to input number of courses first.\n")
        elif option == '5':
            if len(students) > 0 and len(courses) > 0:
                marks = input.input_marks(stdscr, students, courses)
            else:
                stdscr.addstr("You need to input student and course info first.\n")
        elif option == '6':
            output.list_students(stdscr, students)
        elif option == '7':
            output.list_courses(stdscr, courses)
        elif option == '8':
            output.list_marks(stdscr, marks)
        elif option == '9':
            output.sort_students_by_gpa(stdscr, students)
        elif option == '10':
            t = threading.Thread(target=save_data, args=(students, courses, marks))
            t.start()
            t.join()
            break
        else:
            stdscr.addstr("Invalid option. Please try again.\n")

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)