from student_class import Student
from course_class import Course
from teacher_class import Teacher

class School:
    def __init__(self, school_name):
        self.name = school_name
        self.courses = []
        self.students = []
        self.teachers = []

    def __repr__(self):
        return 'There are currently {students_count} students enrolled and {teachers_count} teachers. The school offers {courses_count} courses'.format(students_count=len(self.students), teachers_count=len(self.teachers), courses_count=len(self.courses))

    def add_course(self, course):
        self.courses.append({'Course name': course.name,
                             'Course duration (semesters)': course.duration,
                             'Pass grade (/100)': course.pass_grade,
                             'Enrolled students': course.students_enrolled})

    def add_student(self, student):
        self.students.append({'Student name': student.name,
                             'Student age': student.age, 'Student grade': student.grade})

    def add_teacher(self, teacher):
        self.teachers.append(
            {'Teacher name': teacher.name, 'Subject': teacher.subject})


student_one = Student('Jack', 'male', 15, 8)
student_two = Student('Mary', 'female', 14, 8)

course_one = Course('Biology', 2, 75)
course_two = Course('Math', 2, 60)

teacher_one = Teacher('Doe', 'Biology')
teacher_two = Teacher('C', 'Math')

my_school = School('Park School')

my_school.add_course(course_one)
my_school.add_course(course_two)

my_school.add_student(student_one)
my_school.add_student(student_two)

my_school.add_teacher(teacher_one)
my_school.add_teacher(teacher_two)

teacher_two.enroll_student(student_one, course_two)
teacher_two.enroll_student(student_two, course_two)

teacher_one.enroll_student(student_two, course_one)
teacher_one.enroll_student(student_one, course_one)

teacher_one.enroll_student(student_one, course_two)

teacher_one.give_mark(student_one, 'A')
teacher_two.give_mark(student_one, 'A')

print(student_one)

print(my_school.courses)
print(my_school.students)
print(my_school.teachers)

