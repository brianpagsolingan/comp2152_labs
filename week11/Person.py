class Person:
    def __init__(self, p_name, p_age, p_height):
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I am a public prop"
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector has automatically destroyed the Person object")


person1 = Person("Bobby", 12, 150)
print("name of the person is: " + person1.name)
person1.name= "brian"
print("name of the person is: " + person1.name)
