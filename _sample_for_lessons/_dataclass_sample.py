from dataclasses import dataclass

@dataclass
class Person():
    name:str
    surname:str
    age:int

    def sayHello(self):
        print(self.name,'говорит: "Привет!"')


class OldPerson():
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def sayHello(self):
        print(self.name,'говорит: "Привет!"')

