"""
crear un diccionario con la siguiente información, que segun los casos me diga que tipo de animal es:

Si un animal vuela, es de sangre caliente y se alimenta de sangre, es un murciélago.
Si un animal vuela, es de sangre caliente y no se alimenta de sangre, es un ave.
Si un animal vuela y no es de sangre caliente, es un insecto.
Si un animal no vuela, no debe asignarse a ninguna categoría: sólo nos interesan los animales que vuelan.
"""

animal ={
    "vuela": True,
    "sangre_caliente":True,
    "alimento_sangre":True
    }

if animal["vuela"] == True:
    if animal["sangre_caliente"] == True:
        if animal["alimento_sangre"] == True:
            print("El animal es un murcielago")
        else:
            print("El animal es un ave")
    else:
        print("El animal es un insecto")
else:
    print("No pertenece a ninguna categoria porque el animal no vuela")
