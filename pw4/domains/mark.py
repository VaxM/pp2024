import math

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"Mark for student {self.student.id} in course {self.course.id}: {self.mark}"