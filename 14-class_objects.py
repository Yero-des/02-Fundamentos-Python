# Class objects in Python
import datetime

class Person:
    def __init__(self, name: str, age: int, programming_languages: list, working_experience: int):
        self.name = name
        self.age = age
        self.programming_languages = programming_languages
        self.working_experience = working_experience

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def programming_language(self):
        return f"{self.name} knows the following programming languages: {', '.join(self.programming_languages)}"

    def year_of_entry(self):
        current_year = datetime.datetime.now().year
        entry_year = current_year - self.working_experience
        return f"{self.name} started working in the year {entry_year}."
    

# Creating an instance of the Person class
person1 = Person("Alice", 30, ["Python", "JavaScript", "C++"], 5)
person2 = Person("Yesenia", 48, ["Java", "C#", "Ruby"], 10)

print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person1.programming_language())  # Output: Alice knows the following programming languages: Python, JavaScript, C++
print(person1.year_of_entry())  # Output: Alice started working in the year 2019.

print(person2.greet())  # Output: Hello, my name is Yesenia and I am 48 years old.
print(person2.programming_language())  # Output: Yesenia knows the following programming languages: Java, C#, Ruby
print(person2.year_of_entry())  # Output: Yesenia started working in the year