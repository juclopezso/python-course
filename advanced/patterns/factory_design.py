# Object oriented design pattern
# The goal of OODP is usually to increase the modularity and separation of concerns
# Factory design pattern helps to decide during runtime which particular instance we want to create

from abc import ABCMeta, abstractstaticmethod

# abstract class
# an interface is just a definition of the signature
class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface method """


class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid type")
        return -1


if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()

