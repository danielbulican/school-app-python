class Course:
    def __init__(self, course_name, course_duration, course_pass):
        self.name = course_name
        self.duration = course_duration
        self.pass_grade = course_pass
        self.students_enrolled = []

    def __repr__(self):
        description = 'Welcome to the {name} class. This class will last {duration} semesters. To pass you need a score of {pass_score}.'.format(
            name=self.name, duration=self.duration, pass_score=self.pass_grade)
        if len(self.students_enrolled) > 0:
            description += 'There are currently {students} students enrolled in this course'.format(
                students=len(self.students_enrolled))
        else:
            description += 'There are currently no students enrolled in this course'

        return description


    def see_all_students(self):
        print('These are the names of the students currently enrolled in this {name} course: '.format(
            name=self.name))
        for student in self.students_enrolled:
            print(student)
