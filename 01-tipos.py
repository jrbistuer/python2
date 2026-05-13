print("Hola mundo!")

# Comentario simple

"""
Comentario
multilínea """

"""
Tipos de datos primitivos en Python:
- str: cadenas de texto
- int: números enteros
- float: números decimales
- bool: valores booleanos (True o False)
- None: valor nulo o ausencia de valor
- complex: números complejos
"""

"""Ejemplos de cada tipo de dato:"""

# str
nombre: str = "Juan"
print(nombre)
print("Hola " + nombre)
print(f"Hola {nombre}")
sentence: str = f"Hola {nombre}"
multiline_sentence: str = """Para textos largos, se pueden usar comillas triples.
    Esto permite escribir en varias líneas sin necesidad de usar caracteres de escape.
    ¡Hola mundo!"""
print(multiline_sentence)
print(sentence)
sentence2: str = "Hola {} con asignación posicional"
print(sentence2.format(nombre))
sentence3: str = "Hola {} {}"
name: str = "Juan"
last_name: str = "Pérez"
print(sentence3.format(name, last_name))
sentence4: str = "Hola {name} {last_name}"
print(sentence4.format(name=name, last_name=last_name))
sentence5: str = "Hola {1} {0} con asignación posicional"
print(sentence5.format(name, last_name))
name2: str = "maría de gonzález"
print(name2.capitalize())
print(name2.upper())
print(name2.lower())
print(name2.title())
print(name2.swapcase())
print(name2.replace("maría", "ana"))
print(name2.find("gonzález"))
print(name2.split())

# int & float
edad: int = 30
print(edad)
print(edad + 5)
altura: float = 1.75
print(altura)
print(altura + 0.25)
print((altura + 0.25) + 2)
precio = 19.99
iva = 0.21
precio_con_iva = precio + (precio * iva)
print(precio_con_iva)
print(round(precio_con_iva, 2))
# operaciones
print(10 + 5)  # suma
print(10 - 5)  # resta
print(10 * 5)  # multiplicación
print(10 / 5)  # división
print(10 // 5)  # división entera
print(10 / 3)  # división con decimales
print(10 // 3)  # división entera
print(17 / 3) # división con decimales
print(17 // 3) # división entera
print(10 % 3)  # módulo
print(10 ** 2) # potencia
edad: int = 30

# bool
like_coffee: bool = True
like_tea: bool = False
print(like_coffee)
print(like_tea + 1)  # True se interpreta como 1, False como 0
print(like_coffee + 1)  # True se interpreta como 1, False como 0
print(like_coffee and like_tea)  # False
print(like_coffee or like_tea)  # True
print(like_coffee and 1)  # 1
# Truthy y Falsy
print(bool(0))  # Falsy
print(bool(1))  # Truthy
print(bool(""))  # Falsy
print(bool("Hola"))  # Truthy
print(bool([]))  # Falsy
print(bool([1, 2, 3]))  # Truthy

# None
valor_nulo: None = None
print(valor_nulo)
if valor_nulo == None: # No es recomendable usar '== None', se recomienda usar 'is None' por ser más explícito y 
    # evitar errores de comparación con otros valores que podrían ser considerados falsy.
    print("El valor es nulo")
else:
    print("El valor no es nulo")
if valor_nulo is None: # Recomendado
    print("El valor es nulo")
else:
    print("El valor no es nulo")

# casting
numero_str: str = "123"
print(numero_str)
numero_int: int = int(numero_str)
print(numero_int)
print(numero_str + "4") # Concatenación de strings
print(numero_int + 4) # Suma de enteros
print(numero_str + str(4)) # Concatenación de strings
numero_float: float = float(numero_str)
print(numero_float)
cast_bool: bool = bool(numero_str)
print(cast_bool) # Cualquier string no vacío se considera True