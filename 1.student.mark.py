def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info(num_students):
    students = {}
    for _ in range(num_students): 
        print("====================================================================")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students[id] = (name, dob)
    return students

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info(num_courses):
    courses = {}
    for _ in range(num_courses):
        print("====================================================================")
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses[id] = name
    return courses

def input_marks_for_course(courses, students):
    course_id = input("Enter course id to input marks: ")
    if course_id not in courses:
        print("Invalid course id")
        return None, None

    marks = {}
    for student_id in students:
        mark = input(f"Enter mark for student {student_id}: ")
        marks[student_id] = mark

    return course_id, marks

def list_students(students, course_marks):
    for id, info in students.items():
        print(f"Student ID: {id}, Student Name: {info[0]}, DoB: {info[1]}")
        for course_id, marks in course_marks.items():
            if id in marks:
                print(f"Mark for course {course_id}: {marks[id]}")

def list_courses(courses):
    for id, name in courses.items():
        print(f"Course ID: {id}, Course Name: {name}")

def main():
    students = {}
    courses = {}
    course_marks = {}
    num_students = 0
    num_courses = 0

    while True:
        print("====================================================================")
        print("1. Input number of students")
        print("2. Input student info")
        print("3. Input number of courses")
        print("4. Input course info")
        print("5. Input marks for course")
        print("6. List students")
        print("7. List courses")
        print("8. Exit")

        option = input("Choose an option: ")

        if option == '1':
            num_students = input_number_of_students()
        elif option == '2':
            if num_students > 0:
                students = input_student_info(num_students)
            else:
                print("You need to input number of students first.")
        elif option == '3':
            num_courses = input_number_of_courses()
        elif option == '4':
            if num_courses > 0:
                courses = input_course_info(num_courses)
            else:
                print("You need to input number of courses first.")
        elif option == '5':
            if num_students > 0 and num_courses > 0:
                course_id, marks = input_marks_for_course(courses, students)
                if course_id and marks:
                    course_marks[course_id] = marks
            else:
                print("You need to input student and course first.")
        elif option == '6':
            if num_students > 0:
                list_students(students, course_marks)
            else:
                print("You need to input student info first.")
        elif option == '7':
            if num_courses > 0:
                list_courses(courses)
            else:
                print("You need to input course first.")
        elif option == '8':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()