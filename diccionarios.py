"""
Los diccionarios son un tipo de estructuras de datos que permiten guardar un conjunto no ordenado de pares clave-valor, 
existiendo las claves únicas dentro de un mismo diccionario (es decir, que no pueden tener dos elementos con una misma clave).
 El diccionario se declara entre los caracteres '{ }' y los elementos se separan por comas (',').

Los diccionarios denominados dict para Python, son estructuras de datos muy extendidos en otros lenguajes de programación,
 aunque en otros lenguajes como java se les denominan con distintos nombres como "Map".
"""
# Defino la variable 'futbolistas' como un diccionario.
futbolistas = dict()

futbolistas = {

13 : "Mina", 21 : "Lucumi",

17 : "Fabra", 11 : "Cuadrado",

9 : "Falcao", 19 : "Muriel",

15 : "Uribe", 10 : "James Rodriguez",

16 : "Lerma", 5 : "Wilmar Barrios",

3 : "Murillo"

}
print(futbolistas)
print(futbolistas[10])
