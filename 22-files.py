# Files in python
try:
        
    with open('test2.txt', mode="w") as my_file:
        text = my_file.write(":) ")
        
    with open('test2.txt', mode="r") as my_file:
        print(my_file.readlines())
        
    # Lee y luego escribe
    with open('test2.txt', mode="r+") as my_file:
        print(my_file.readlines())
        text = my_file.write("Hola mundo")
    
    # (Append) agrega lo que escribamos hasta el final del texto
    with open('test2.txt', mode="a") as my_file:
        text = my_file.write("My name is yeromi")
        print(text)
        
        
except FileNotFoundError: print("El archivo no existe.")
except Exception as e:
    print(f"Ocurrió un error: {e}")