# the class can only have one single instance 

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """Implement in child class"""


class PersonSingleton(IPerson):

    # private variable
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            return PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot ve instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self


    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

p2 = PersonSingleton("Bob", 20) # this will fail
print(p2)
