# Decorators in Python
def require_auth(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user').lower()
        password = kwargs.get('password').lower()
        
        if user == "admin" and password == "123":
            return func(*args, **kwargs)
        else:
            return "Access denied"
        
    return wrapper

@require_auth
def admin_dashboard(*args, **kwargs):
    user = kwargs.get('user')
    return f"Bienvenido al panel, {user}"

print(admin_dashboard(user="Admin", password="123"))  # Output: Bienvenido al panel, admin
print(admin_dashboard(user="Admin", password="13414"))  # Output: Access denied
print(admin_dashboard(user="ADMIN", password="123"))  # Output: Access denied
print(admin_dashboard(user="Guest", password="123"))  # Output: Access denied


def uppercase_word(func):
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapped

@uppercase_word
def greet(word):
    return f"Hello, {word}!"

print(greet("world"))  # Output: HELLO, WORLD!

person1 = {
    "name": "Yeromi",
    "age": 21,
    "dni": "75880289"
}

# You can access dictionary values using both indexing and the get method
print(person1)
print(f"Hi my name is {person1['name']} and I am {person1['age']} years old.")
print(f"Hi my name is {person1.get('name')} and I am {person1.get('age')} years old.")
print(f"My DNI is {person1['dni']}.")
print(f"My DNI is {person1.get('dni')}.")