def list_students(stdscr, students):
    if len(students) == 0:
        stdscr.addstr("No students to list. Input student info first.\n")
        return
    for student in students:
        stdscr.addstr(str(student) + "\n")

def list_courses(stdscr, courses):
    if len(courses) == 0:
        stdscr.addstr("No courses to list. Input course info first.\n")
        return
    for course in courses:
        stdscr.addstr(str(course) + "\n")

def list_marks(stdscr, marks):
    if len(marks) == 0:
        stdscr.addstr("No marks to list. Input marks for course first.\n")
        return
    for mark in marks:
        stdscr.addstr(str(mark) + "\n")

def sort_students_by_gpa(stdscr, students):
    students = sorted(students, key=lambda student: student.calculate_gpa(), reverse=True)
    for student in students:
        stdscr.addstr(f"{student} GPA: {student.calculate_gpa()}\n")