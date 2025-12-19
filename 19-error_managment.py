# Error managment in Python
def divide_numbers():
    try:
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el denominador (no puede ser 0): "))
        result = a / b
    
    except ZeroDivisionError: print("No se puede dividir entre cero.")
    except ValueError: print("Por favor ingresa solo numeros")
    except Exception as error: print(type(error))
    # It always execute if there is not problems
    else: 
        print(result)
        return result
    # It always execute if there is a problem or not
    finally: 
        print("Gracias por usar nuestra calculadora")
        
divide_numbers()