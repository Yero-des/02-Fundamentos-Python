# Attributes and methods in Python
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100  # Protected attribute
        self.__password = "12345"  # Private attribute
    
    def work(self):
        return f"{self.name} esta trabajando duro"
    
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
    
    def __generate_password(self):
        return f"$${self.name}{self.age}$$"
        
    
person1 = Person("Juan", 30)
print(person1.work())
print(person1._waste_energy(20))
print(person1._Person__password)  # Accessing private attribute using name mangling
print(person1._Person__generate_password())  # Accessing private method using name mangling