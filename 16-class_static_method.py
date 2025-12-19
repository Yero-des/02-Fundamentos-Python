# Class static method in Python
class Person: 
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    """ You can use @classmethod to define a method that modifies class attributes.
    This method can be called on the class itself or on instances of the class ejm:
    -   Person.change_species("Reptiliano")
    """
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    """ You can use @staticmethod to define a method that does not modify class or instance
    attributes. This method can be called whithout an instance ejm:
    -   Person.is_older(18)
    """
    @staticmethod
    def is_older(age):
        return age >= 18

person1 = Person("Ricardo", 25)
person2 = Person("Ana", 28)

print(person1.species)  # Accessing class attribute via instance
print(person2.species)

# Changing species using class method
Person.change_species("Reptiliano")

print(person1.species)  # Accessing class attribute via instance
print(person2.species)

print(Person.is_older(20))  # Using static method
print(Person.is_older(15))
