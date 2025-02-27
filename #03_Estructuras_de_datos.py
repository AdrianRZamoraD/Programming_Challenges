"""/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 """


# listas

my_list = ["Adrian", "Ricardo", "Ana", "Gabriela"] # [] son listas
print(my_list)
print(type(my_list))
my_list.append("Neto")      # inserction
my_list.append("Neto")      # Se puede añadir otro dato igual
print(my_list)              # tipo de dato
my_list.remove("Adrian")    # Eliminación
print(my_list)
print(my_list[1])           # Acceso
my_list[1] = "Zamora"       # Actualización
my_list.sort()              # Orden por defecto alfabeticamente
print(my_list)

# Tuplas    , se puede guardar mas de un dato son inmutables (no se pueden realizar modificaciones)

my_tuple: tuple = ("Adrian", "Zamora", "@AdrianZ", "31") # se cambia el int por str para que funcione el sorted porque se confunde.
print(type(my_tuple))
print(my_tuple[0])                  # Acceso
print(my_tuple[1])
my_tuple = tuple(sorted(my_tuple))  # Se le da un valor, tuple para que se vuelva tupla, sorted para acomodar alfabeticamente pero lo convierte a lista
print(my_tuple)
print(type(my_tuple))

# Sets  , estrucrura desordenada, no sirve para buscar datos, no deja insetar duplicados, para realizar una actualización lo correcto es eliminar el dato y volverlo a insertar

my_set = {"Adrian", "Zamora", "@AdrianZ", "31"}
print(my_set)
print(type(my_set))
my_set.add("Ana")       # inserción en orden al azar
my_set.add("Ana")       # No deja guardar datos duplicados, simplemente lo analiza y no lo guarda
my_set.add("Kytra")
print(my_set)
my_set.remove("Adrian") # Eliminación
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario

my_dictionary: dict = {
    "name":"Adrian", 
    "surname": "Ricardo", 
    "email":"AdrianZ@.com", 
    "age":"31"
    }
print(type(my_dictionary))
print(my_dictionary)
my_dictionary["alias"] = "Azwors"   # Insercción
print(my_dictionary)
my_dictionary["age"] = "40"         # Actualización
print(my_dictionary)
print(my_dictionary["name"])        # Acceso
del my_dictionary["alias"]          # Eliminación
my_dict = dict(sorted(my_dictionary.items()))   # ordenación, items me devuelve todas las claves y valores
print(my_dict)
print(type(my_dict))

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */"""


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el numero del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) < 11:
            agenda[name] = phone
            print("Contacto actualizado")
        else:
            print("Debes introducir un número de teléfono un máximo de 11 digitos")

    while True: # Siempre es verdadero, se ejecuta infinitamente

        print("1. buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("4. Salir")

        option = input("\nSelecciona una opción: ") # Para que el usuario interactua con la terminal

        match option:   # match desde la versión 3.10
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El número de telefono de {name} es {agenda[name]}")
                else:
                    print("Debes introducir un nombre válido. ")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Instroduce el nombre del contacto")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar")
                if name in agenda:
                    print(f"El contacto {name} con su número de teléfono {agenda[name]} ha sido Eliminado")
                    del agenda[name]    
                else:
                    print("El contacto que has introducido no es válido")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()