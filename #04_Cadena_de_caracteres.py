"""/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *"""

### Operaciones ###

s1 = "Hola"
s2 = "Python"

# Concatenación

print(s1 + s2) # HolaPython
print(s1 + ", " + s2 + "!") # Hola, Python!

# Repetición

print(s1 * 3)    # HolaHolaHola

# Indexación

print(s1[0])     # H
print(s1[0] + s1[1] + s1[2] + s1[3])    # Hola

# Longitud

print(len(s1))   # 4

# Slicing (porción)

print(s2[2:5])  # tho
print(s2[2:])   # thon
print(s2[0:2])  # Py
print(s2[:2])   # Py

# Búsqueda

print("a" in s1)    # True
print("i" in s1)    # False

# Reemplazar

print(s1.replace("o", "a")) # Hala

# División

print(s2.split("t"))    # ['Py', 'hon'] Se obtienen 2 elementos

# mayúsculas, minúsculas y letras en mayúsculas

print(s1.upper())
print(s1.lower())
print("adrian zamora".title())      # Adrian Zamora ambas primeras letras en mayúsculas
print("adrian zamora".capitalize()) # Adrian zamora solo la primera letra en mayúsculas de la primera palabra

# Eliminación de espacios al principio y al final

print(" adrian zamora ".strip() + "@AdrianZ.com")   # adrian zamora@AdrianZ.com, elimina los espacios al principio y al final
print(" adrian zamora " + "@AdrianZ.com")           # adrian zamora @AdrianZ.com

# Busqueda al principio y al final
print(s1.startswith("Ho"))  # True
print(s1.startswith("Py"))  # False
print(s1.endswith("la"))    # True
print(s1.endswith("thon"))  # False

# Búsqueda de posición

s3 = "Adrian Zamora @adrianzamo"

print(s3.find("zamo"))      # 21
print(s3.find("Zamo"))      # 7
print(s3.find("z"))         # 21
print(s3.find("Z"))         # 7
print(s3.lower().find("z")) # 7

# Búsqueda de ocurrencias, cantidad de veces de aparición

print(s3.lower().count("z"))    # 2

# Formteo

print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación

print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista de caracteres

print(list(s3)) # ['A', 'd', 'r', 'i', 'a', 'n', ' ', 'Z', 'a', 'm', 'o', 'r', 'a', ' ', '@', 'a', 'd', 'r', 'i', 'a', 'n', 'z', 'a', 'm', 'o']

# Transformación de lista en cadena
l1 = [s1 , ", ", s2, "!"]   # ['Hola', ', ', 'Python', '!']
print(l1)
print("".join(l1))          # Hola, Python!
print("-".join(l1))         # Hola-, -Python-!

# Transformaciones numéricas

s4 = "123456"       
s4 = int(s4)        # 123456 a Int
print(s4)

s5 = "123456.123"
s5 = float(s5)      # 123456.123 Float
print(s5)

# Comprovaciones varias

s4 = str(s4)

print(s1.isalnum())     # alfanumérico, True contiene letras o números
print(s1.isalpha())     # solo letras, True
print(s4.isalpha())     # Error si no se vuelve a convertir el valor de s4 en Str, False porque se convirtio a texto
print(s4.isnumeric())   # True 

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos    se lee igual de adelante hacia atrás ejemplo: anilina, arriba la birra
 * - Anagramas      Cambio en el orden de las letras de una palabra o frase que da lugar a otra palabra o frase distinta ejemplo amor - roma, imán - maní(con acentos no funciona el sorted de manera esperada)
 * - Isogramas      no se repite la misma letra
 */
 """

def my_function (Str1, Str2: str):
 
    # Palíndromos
    
    if Str1 == Str1[::-1]:
        print(f"{Str1} es Palíndromo")
    if Str2 == Str2[::-1]:
        print(f"{Str2} es Palíndromo")
    if Str1 != Str1[::-1]:
        print(f"{Str1} no es Palíndromo")
    if Str2 != Str2[::-1]:
        print(f"{Str2} no es Palíndromo")

    # print(f"¿{Str1} es palíndromo?: {Str1 == Str1[::-1]}")    # otra forma de escribir el código
    # print(f"¿{Str2} es palíndromo?: {Str2 == Str2[::-1]}")

    # Anagramas

    print(f"¿{Str1} y {Str2} son anagramas?: {sorted(Str1) == sorted(Str2)}")

    # Isogramas

    def isogram(word: str) -> bool:    

        word_dict = dict()
        for word in Str1:
            word_dict[word] = word_dict.get(word, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{Str1} es un Isograma?: {isogram(Str1)}")
    print(f"¿{Str2} es un Isograma?: {isogram(Str2)}")


my_function("amor","roma")