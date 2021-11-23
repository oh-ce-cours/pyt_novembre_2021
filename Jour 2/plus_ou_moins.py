def my_input():
    """
    On demande un nombre à l'utilisateur tant que son entrée est invalide
    Version 1 : on regarde où on marche (on fait en sorte d'éviter l'exception)
    """
    res = None

    while res is None:
        inputed = input("Veuillez entrer un nombre: ")
        if inputed.isnumeric():
            res = int(inputed) 
            return res 
        else:
            print("J'ai dit un nombre!!!!!!!!!")

def my_input_2():
    """
    On demande un nombre à l'utilisateur tant que son entrée est invalide
    Version 2 : on demande pardon plutot que la permission (si l'exception se produit, on la règle)
    """
    res = None

    while res is None:
        inputed = input("Veuillez entrer un nombre: ")
        try:
            res = int(inputed) 
        except ValueError:
            print("J'ai dit un nombre!!!!!!!!!")
            res = None 
        else:
            return res

import random


NOMBRE_A_TROUVER = random.randint(1, 100)
nombre_entre = 
print(nombre_entre)
while (nombre_entre := my_input_2()) != NOMBRE_A_TROUVER:
    if nombre_entre > NOMBRE_A_TROUVER:
        print("c'est moins")
    else:
        print("c'est plus")
    nombre_entre = my_input_2()
print("c'est fini")

# while True:
#     if nombre_entre > NOMBRE_A_TROUVER:
#         print("c'est moins")
#     elif nombre_entre < NOMBRE_A_TROUVER:
#         print("c'est plus")
#     else:
#         break 
#     nombre_entre = my_input_2()
# print("c'est fini")
