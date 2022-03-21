# school-app-python

This simple program written in python can allow a school keep track of its students, courses and teachers. It contains 4 classes: Student, Course, Teacher and School. 

The Student class allows to create an object that stores personal information about a student. When this class is called it returns details about the student like his or her name, grade and courses they follow.

The Teacher class stores details about the teacher like their name, subject they teach and a list of the marks they have given. This class contains two methods: give_mark() and enroll_student(). The first method allows a teacher to give marks to a student. Doing so will add an object to the student's list of marks containing the subject name and mark given. With the second method a teacher can enroll a student on a course, but only if the course subject is the same as the one they teach.

The Course class stores information like the course name, duration, pass grade and a list containing the students enrolled. 

Finally, the School class can be used to store general informaton about all the students, courses and teachers in the shcool. It stores this information as objects.

