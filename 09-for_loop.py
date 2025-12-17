# For loop en Python — ejemplos
# my_list = [10, 20, 30, 40, 50]
# addition = 0

# for number in my_list:
#   addition += number

# print("La suma es:", addition)

for index, number in enumerate(list(range(1, 101))):
  print(index, number)