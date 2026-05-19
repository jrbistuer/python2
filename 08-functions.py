def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"

print(saludar("Juan"))  # Printing the result of the saludar function with the argument "Juan"

def saludar2(nombre: str, apellido: str) -> None:
    print(f"Hola, {nombre} {apellido}!")

saludar2("Juan", "Pérez")  # Printing the result of the saludar2 function with the arguments "Juan" and "Pérez"

def sumar(num1: int, num2: int = 10) -> int:
    return num1 + num2

resultado = sumar(5, 15)  # Storing the result of the sumar function with the arguments 5 and 15 in the variable resultado
print(resultado)  # Printing the value of resultado
resultado2 = sumar(5)  # Storing the result of the sumar function with the argument 5 in the variable resultado2
print(resultado2)  # Printing the value of resultado2

def multiplicar(*args: int) -> int:
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

resultado3 = multiplicar(2, 3, 4)  # Storing the result of the multiplicar function with the arguments 2, 3, and 4 in the variable resultado3
print(resultado3)  # Printing the value of resultado3

# **kwargs — variable keyword arguments
def imprimir_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")
imprimir_info(nombre="Juan", apellido="Pérez", edad="30")  # Printing the result of the imprimir_info function with the keyword arguments nombre, apellido, and edad