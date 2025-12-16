# List in python
list_numbers = [1, 2, 3, 4, 5]
list_letters = ['a', 'b', 'c', 'd', 'e']
list_mix = [2, 'x', 1, 'z', 3.5, True]

shopping_cart = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

print(type(shopping_cart))

# Methods of list
# append
print(shopping_cart)
shopping_cart.append('Ram 8GB')
shopping_cart.append('Mouse')
print(shopping_cart)

# remove
shopping_cart.remove('Keyboard')
print(shopping_cart)

# count 
print(shopping_cart.count('Laptop')) # helps to count how many times an element is present in the list
print(shopping_cart.count('Mouse'))
print(shopping_cart.count('Grafica'))
