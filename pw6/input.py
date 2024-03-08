import curses

def input_students(stdscr, num_students):
    students = []
    for _ in range(num_students):
        stdscr.addstr("================================================\n")
        stdscr.addstr("Enter student id: ")
        id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Enter student name: ")
        name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Enter student DoB: ")
        dob = stdscr.getstr().decode('utf-8')
        students.append(Student(id, name, dob))

    with open('students.txt', 'w') as f:
        for student in students:
            f.write(f'{student.id},{student.name},{student.dob}\n')

    return students

def input_courses(stdscr, num_courses):
    courses = []
    for _ in range(num_courses):
        stdscr.addstr("================================================\n")
        stdscr.addstr("Enter course id: ")
        id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Enter course name: ")
        name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Enter course credit: ")
        credit = int(stdscr.getstr().decode('utf-8'))
        courses.append(Course(id, name, credit))

    with open('courses.txt', 'w') as f:
        for course in courses:
            f.write(f'{course.id},{course.name},{course.credit}\n')

    return courses

def input_marks(stdscr, students, courses):
    marks = []
    stdscr.addstr("================================================\n")
    stdscr.addstr("Enter course id to input marks: ")
    course_id = stdscr.getstr().decode('utf-8')
    course = next((course for course in courses if course.id == course_id), None)
    if course is None:
        stdscr.addstr("Invalid course id\n")
        return marks

    for student in students:
        stdscr.addstr(f"Enter mark for student {student.id}: ")
        mark = float(stdscr.getstr().decode('utf-8'))
        mark = math.floor(mark * 10) / 10  # round down to 1 decimal place
        mark_obj = Mark(student, course, mark)
        marks.append(mark_obj)
        student.marks.append(mark_obj)  # add mark to student's marks

    with open('marks.txt', 'w') as f:
        for mark in marks:
            f.write(f'{mark.student.id},{mark.course.id},{mark.mark}\n')

    return marks