from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        super().__init__(p_name, p_age, p_height)
        self.__major = p_major
        print("This time it's a student object")


student1 = Student("bob", 12, 100, "fashion")
print("name of the student is: " + str(student1.name))
print("major of the person is: " + str(student1.major))


