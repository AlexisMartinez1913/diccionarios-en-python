"""
Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.
"""

def cargar():
    diccionario = {}
    continua = "s"
    while continua=="s":
        español = input("Ingrese la palabra en castellano: ")
        ingles = input("Ingrese su traducción en ingles: ")
        diccionario[ingles]=español
        continua=input("Desea agregar más palabras? [s/n]: ")
    return diccionario

def mostrar(diccionario):
    print("Listado completo: ")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def traduccion(diccionario):
    palabra = input("Ingrese una palabra en ingles a consultar: ")
    if palabra in diccionario:
        print("En castellano significa: ", diccionario[palabra])

#bloque principal
diccionario = cargar()
mostrar(diccionario)
traduccion(diccionario)

