# While in python
# counter = 1

# while counter <= 5:
#     print(f"Number: {counter}")
#     counter += 1
# else:
#     print("Terminamos el ciclo while")

response = ''
vocals = ('a', 'e', 'i', 'o', 'u')

while response.lower() != 'bye':
    response = input("Type a word to analyze (bye to exit): ")
    if response != 'bye':
        print(f"The first letter is: {response[0]}")
        print(f"The last letter is: {response[-1]}")
        print(f"The length of your input is: {len(response)} letters")
        for vocal in vocals:
            if vocal in response.lower():
                print(f"The letter '{vocal}' is present in your input.")
else:
    print("You have exited the loop.")