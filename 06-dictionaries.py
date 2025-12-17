# Dictionaries in Python
user = {
  "name": "Yeromi",
  "age": 21,
  "is_student": False,
  "courses": ["Math", "Science", "Art", "Programming"],
  "languages" : ["Espanish", "English"],
  "email" : "yero@hotmail.com",
  (19.12, -98.34) : "Coordinates" # You only can have a tuple as a key in your dictionary
}

user["age"] = 22
user["email"] = "yeromi123@gmail.com"
user["country"] = "Perú" # You can add a new key-value pair to the dictionary

# print(user[(19.12, -98.34)])

#values, items, keys
# print(user.items())
# print(user.keys())
# print(user.values())

