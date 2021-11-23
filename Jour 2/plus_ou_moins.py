import random

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

NOMBRE_A_TROUVER = random.randint(1, 100)


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

def soluution_1():
    while (nombre_entre := my_input_2()) != NOMBRE_A_TROUVER:
        if nombre_entre > NOMBRE_A_TROUVER:
            print("c'est moins")
        else:
            print("c'est plus")
    print("c'est fini")

def solution_2():
    while True:
        if nombre_entre > NOMBRE_A_TROUVER:
            print("c'est moins")
        elif nombre_entre < NOMBRE_A_TROUVER:
            print("c'est plus")
        else:
            break 
        nombre_entre = my_input_2()
    print("c'est fini")

def solution_3_nicolas():
    def input_int(question):
        nb = input("Proposition ? ")
        if nb.isnumeric():
            return int(nb)
        print("Mauvaise saisie")
        return 0

    nombre_ordinateur = random.randint(1, 10)
    print("J'ai choisi un nombre entre 1 et 10, devinez le ?")

    nombre_utilisateur = 0

    while nombre_utilisateur != nombre_ordinateur:
        # Saisie
        nombre_utilisateur = input_int("Proposition ? ")
        if not nombre_utilisateur:
            continue

        # Vérification
        if nombre_utilisateur < nombre_ordinateur:
            print("C'est Plus")
        if nombre_utilisateur > nombre_ordinateur:
            print("C'est Moins")

    print("Bravo, c'était bien ", nombre_ordinateur)

solution_1()