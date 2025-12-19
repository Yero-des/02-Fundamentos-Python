# Functions in Python
# def greet(greet = "Hi", name = "Customer"):
#     print(f"{greet}, {name}!")

# # Calling the function
# greet("Hello", "Yeromi")
# greet("Ey dude", "Yeromi")
# greet()  # Using default parameters
# greet(name="Eduardo", greet="Hola")  # Using named arguments

def big_function(*args, **kwargs):
    print(type(args), args) # <class 'tuple'>
    print(type(kwargs), kwargs) # <class 'dict'>
    return kwargs

print(big_function(1, 2, 3, name="Yeromi", age=25))