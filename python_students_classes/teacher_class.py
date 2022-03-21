class Teacher:
    def __init__(self, teacher_name, teacher_subject):
        self.name = teacher_name
        self.subject = teacher_subject
        self.marks_given = []

    def __repr__(self):
        return 'This is teacher {name}. They teach {subject}'.format(name=self.name, subject=self.subject)

    def give_mark(self, student, mark):
        student.marks.append({self.subject: mark})
        self.marks_given.append({student.name: mark})

    def enroll_student(self, student, course):
        if course.name == self.subject:
            course.students_enrolled.append(student.name)
            student.courses.append(course.name)
        else:
            print("Enrollment in this course is reserved to the course's teacher")



