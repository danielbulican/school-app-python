class Student:
    def __init__(self, student_name, student_gender, student_age, student_grade):
        self.name = student_name
        self.age = student_age
        self.grade = student_grade
        self.gender = student_gender
        self.courses = []
        self.marks = []

    def determine_pronoun(self):
        if self.gender == 'male':
            return 'He'
        else:
            return 'She'

    def __repr__(self):
        description = 'This is {name}. {pronoun} is {age} old. {name} is in {grade}th grade. '.format(
            name=self.name, pronoun=self.determine_pronoun(), age=self.age, grade=self.grade)
        if len(self.courses) > 0:
            description += 'Jack is currenlty studying: '
            for course in self.courses:
                description += course + '\\'

        return description

    def passed_year(self):
        self.grade += 1
        print("{name} passed this year's final exams and is in {grade}th grade now".format(
            name=self.name, grade=self.grade))
