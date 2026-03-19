from abc import ABC, abstractmethod
class Animal(ABC):
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return ("name is " + self.name + " age is " + str(self.age))
    
    @abstractmethod
    def voice(self):
        pass
    

class Dog(Animal):
    breed = None

    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    def voice(self):
        return "gaw"
    
    def __str__(self):
        return super().__str__() +" breed is " + self.breed 
    

class Cat(Animal):
    breed = None

    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    def voice(self):
        return "meaw"
    
    def __str__(self):
        return super().__str__() +" breed is " + self.breed 

class Woolf(Animal):

    def __init__(self, name, age):
        super().__init__(name,age)

    def voice(self):
        return "ayyyy"
    
    def __str__(self):
        return super().__str__() 
