# Person
#from Person import * #get classes from Person file

# object, superclass
class Person(object):

    # constructor, can only be one
    def __init__(self, age = 18, name = "Linus"):
        self.age = age
        self.name = name

    def setAge(self, age):
        self.age = age
    def setName(self, name):
        self.name = name
    def toString(self):
        return "{} is {} years old".format(self.name, self.age)

# Person is superclass
class Student(Person):
    def __init__(self, age = 18, name = "Linus"):
        self.course = 'Computer Science'
        super().__init__(age,name)
    
    def toString(self):
        res = super().toString()
        res += "\nEnrolled on {}".format(self.course)
        return res


####

person = Person()
print(person.toString())

student = Student("21", "Adam")
print(student.toString())