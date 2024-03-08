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