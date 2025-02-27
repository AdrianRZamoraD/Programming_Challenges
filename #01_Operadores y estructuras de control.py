"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */"""

# operadores aritméticos

print(f"Suma: 1 + 2 = {1 + 2}")
print(f"Resta: 4 - 2 = {4 - 2}")
print(f"Multiplicación 4 * 2 = {4 * 2}")
print(f"Exponencial 4 ** 2= {4 ** 2}")
print(f"División: 7 / 2 = {7 / 2}")
print(f"División entera: 7 // 2 = {7 // 2}")
print(f"Módulo: 5 % 2 = {5 % 2}") # nos arroja el residuo que es "1" en este caso porque es lo que sobra después de dividir

# Operadores de comparación

print(f"Igualdad: 2 == 2 es {2 == 2}") # igualdad colocando dos signos "=" (3) True
print(f"Igualdad: 4 == 2 es {4 == 2}") # False porque no es igual
print(f"Diferencia: 6 != 2 es {6 != 2}") # True porque si es diferente
print(f"Diferencia: 2 != 2 es {2 != 2}") # False porque no son diferentes
print(f"Mayor que: 6 > 2 es {6 > 2}")
print(f"Mayor o igual que: 6 >= 2 es {6 >= 2}")
print(f"Menor que: 6 < 2 es {6 < 2}")
print(f"Menor o igual que: 6 <= 2 es {6 <= 2}")

# Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") # cumple con TRUE
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") # cumple una de las condiciones y lanza TRUE
print(f"NOT !: 10 + 3 == 13 not 5 - 1 == 4 es {10 + 3 == 14}")
print(f"NOT !: 10 + 3 == 14 es {not 10 + 3 == 14}") # al añadir not a un false automatico, se vuelve TRUE

# Operadores de asignación

my_number = 11 # asignación
print(my_number)
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 # resta y asignación
print(my_number)
my_number *= 2 # multiplicación y asignación
print(my_number)
my_number /= 2 # división y asignación
print(my_number)
my_number %= 2 # módulo y asignación
print(my_number)
my_number **= 1 # exponente y asignación
print(my_number)
my_number //= 1 # división entera y asignación
print(my_number)

# Operadores de identidad

my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}") # False
print(f"my_number is my_new_number es {my_number is not my_new_number}") # Ture

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}") # True
print(f"my_number is my_new_number es {my_number is not my_new_number}") # False

# Operadores de pertenencia

print(f"'a' in 'Adrian' = {'a' in 'Adrian'} ") # la 'a' pertenece al nombre adrian es TRUE
print(f"'b' not in 'Adrian' = {'b' not in 'Adrian'}" ) # TRUE, la 'b' no pertenece a Adrian

# Operadores de bit

a = 10  # 1010
b = 3   # 0011
print(f"AND: 10 & 3 = {10 & 3}")    # 0010
print(f"AND: a & b = {a & b}")      # 0010
print(f"OR: 10 | 3 = {10 | 3}")     # 1011
print(f"XOR: 10 & 3 = {10 ^ 3}")    # 1001
print(f"NOT: ~10 = {~10}")           
print(f"desplazamiento a la derecha: 10 >> 2  = {10 >> 2}")    # 0010
print(f"desplazamiento a la izquierda: 10 << 2  = {10 << 2}")  # 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "Adrian"    # para que se cumpla la condición
my_string = "Zamora"    # para que se cumpla la condición tiene que fallar el if primero
#my_string = "Nothing"  # para que se cumpla la condición tiene que fallar el if primero, despues elif y se ejecute el else


if my_string == "Adrian":   # "if" si se cumple has algo, sino se cumple has otra cosa
    print("My string es 'Adrian'")
elif my_string == "Zamora":
    print("my string es Zamora")    # condició intermedia   
else:
    print("my string no es 'Adrian' ni 'Zamora'")

# Iterativas

for i in range(11): # para bucles
    print(i)

i = 0

while i <=10:     # bucle infinito si no tiene el i += 1 para alcanzar el 10 y finalizar, tambien se puede usar el BROKE
    print(i)
    i += 1

# Manejo de excepciones

try:
    #print(10/0)
    print(10/1) # aqui no se ejecuta el except
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo."""

"""b = 10

while b <= 55:
    if b == 55:
        print(a)
    elif b == 10:
        print(a)
    elif b == 16:
        not print(a)      
    else:    
        b += 2
        a = b 
        print(ab) """

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
    elif number == 55:
        print(number)


