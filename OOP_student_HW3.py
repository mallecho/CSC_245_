class Student:
    def __init__(self, name, student_id, gpa):
        # Private attributes to ensure encapsulation
        self.__name = name
        self.__student_id = student_id
        self.__gpa = gpa
        self.__attendance = 0  # Private variable for attendance

    # Public method to increment attendance safely
    def mark_attendance(self):
        self.__attendance += 1

    # Public method to retrieve current attendance safely
    def get_attendance(self):
        return self.__attendance

    # Public method to display student details
    def display_info(self):
        print(f"Name: {self.__name}, ID: {self.__student_id}, GPA: {self.__gpa}")

    # Getter methods for name and student_id (if needed by Course class)
    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id


class Course:
    def __init__(self, course_name):
        # Initialize course name and private list for enrolled students
        self.__course_name = course_name
        self.__students = []

    # Public method to enroll a student
    def add_student(self, student):
        self.__students.append(student)
        print(f"Student {student.get_name()} has been added to {self.__course_name}.")

    # Public method to remove a student by student_id
    def remove_student(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                self.__students.remove(student)
                print(f"Student {student_id} has been removed from {self.__course_name}.")
                return
        print(f"Student {student_id} not found in {self.__course_name}.")

    # Public method to list all enrolled students
    def list_students(self):
        print(f"Students enrolled in {self.__course_name}:")
        for student in self.__students:
            student.display_info()





student1 = Student("Alice", "S12345", 3.8)
student2 = Student("Bob", "S67890", 3.5)


course = Course("Computer Science")


course.add_student(student1)
course.add_student(student2)


course.list_students()


student1.mark_attendance()


print("Attendance for Alice:", student1.get_attendance())


course.remove_student("S67890")  #removes Bob from student list


course.list_students()
