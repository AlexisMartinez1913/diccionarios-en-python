"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""
def cargar():
    cedulas = {}
    for x in range(4):
        cc = int(input("Ingrese su # de documento: "))
        nombre = input("Ingrese su nombre: ")
        cedulas[cc]=nombre
    return cedulas

def listado(cedulas):
    print("Diccionario completo: ")
    for cc in cedulas:
        print(cc, cedulas[cc])

def consulta(cedulas):
    cc = int(input("Ingrese el # del documento: "))
    if cc in cedulas:
        print("El nombre al que corresponde este # es: ", cedulas[cc])
    else:
        print("No existe es numero de documento")


#bloque principal
datos = cargar()
listado(datos)
consulta(datos)