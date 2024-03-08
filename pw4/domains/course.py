class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Course ID: {self.id}, Course Name: {self.name}, Credit: {self.credit}"