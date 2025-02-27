"""/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 """

### Funciones definidas por el usuario

# simple

def greet():    
    print("Hola Python")

greet()

# Con retorno

def return_greet():
    return "Hola Python"

greet = return_greet()      # De esta manera se asigna a una variable para mandarla a llamar
print(greet)

print(return_greet())       # De esta manera se llama a la variable para que haga la acción requerida en esta caso el print

# Con un argumento

def arg_greet(name):        # en paréntesis se coloca un argumento para modificar al colocar el mismo valor en el print siguiente
    print(f"Hola {name}!")

arg_greet("Adrian")

# Con un argumentos

def arg_greet(name, surname):        # en paréntesis se coloca un argumento para modificar al colocar el mismo valor en el print siguiente
    print(f"Hola {name}, {surname}!")   # tienen que ser llaves por separado para que imprima bien los string sin añadir paréntesis al print final

arg_greet("Adrian", "Zamora")
arg_greet("Zamora", "Adrian")
arg_greet(surname="Zamora", name="Adrian")  # de esta manera se indica a cual corresponde

# Con un argumento predeterminado

def default_arg_greet(name = "Falta nombre de Usuario"):        
    print(f"Hola {name}!")

default_arg_greet("Adrian")
default_arg_greet()             # AL no escribir nada se coloca el string por defecto asignado

# Con argumentos y retorno

def return_arg_greet(name, surname):        
    return f"{name}, {surname}!"

print(return_arg_greet("Hi", "Adrian"))

# Con retorno de varios valores

def multiple_return_greets():
    return "Hola", "Python"

greet, name = multiple_return_greets()  # al igualar y separar por comas
print(greet)
print(name)

# Con un número variable de argumento

def variable_arg_greet(*names):  # con el "*" asterisco, podemos agregar mas de un nombre
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Adrian", "Ricardo", "Otro mas", "el último")

# Con un número variable de argumentos con palabras clave

def variable_key_arg_greet(**names):  # con el "*" asterisco, podemos agregar mas de un nombre con otro "*" una clave
    for key, name in names.items(): # descompone los elementos en una clave y en un valor
        print(f"{name} ({key})")

variable_key_arg_greet(
    Language="Python",
    name="Adrian",
    alias="Azwors",
    age=31
)

# The pass Statement - pasar declaración

def my_fuction_1():
    pass        # para evadir errores, solo pasa de el

my_fuction_1()


# Positional-Only arguments - posicional-solo argumentos

def my_fuction_po(x, /):
    print(x)

my_fuction_po(5)

def my_function(x):
  print(x)

my_function(x = 3)

#def my_function(x, /):  # error porque solo se puede colocar un valor posicional al agregar la "/""
 # print(x)

#my_function(x = 3)

# Keyword-only arguments - palabra clave, solo argumentos

def my_function(*, x):
  print(x)

my_function(x = 3)

# Funciones dentro de funciones

def outher_fuction():
    def inner_fuction():
        print("Función interna: Hola, Python !")
    inner_fuction()

outher_fuction()

#def my_function(*, x):     error por ser posicional y tener el *
#  print(x)

#my_function(3)

# Combine Positional-Only and Keyword-Only - Combinar posiciones- solo y solo palabra clave
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
    
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


### Funciones del lenguaje (built-in)

print(abs(5.2))     # imprime el valor absoluto de un Int, float, o implementando un objeto con __abs__()
print(len("Adrian_"))    # retorna la longitud del string que son 7 contando el "_"
print(type("Adrian"))   # para ver el tipo de valor(Str, Int, Bool, float, complex, list, tuple, dictionary)
print("Adrian".upper()) # upper para colocar el string en mayúsculas
"""investigar
aiter()
all()
anext()
any()
ascii()
bin()
bool()
breakpoint()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()
"""

"""
Variables locales y globales
"""

global_variable = "Python" # Variable de acceso global

print(global_variable)

def hello_python():
    local_var = "Hola"  # Variable de acceso local
    print(f" {local_var}, {global_variable}!")

hello_python()

# print(local_var) # no se acceder por ser variable local propia de hello_python()


"""* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
 """

def String(String_1, String_2) -> int:
    count = 0
    for String in range(1, 100):
        if String % 3 == 0 and String % 5 == 0:
            print(String_1 + String_2)
        elif String % 3 == 0:
            print(String_1)
        elif String % 5 == 0:
            print(String_2)  
        else:
             print(String)
             count +=1
    return count

print(String("Hello", "Python")) # Al agregar el print se imprime el count final



