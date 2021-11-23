NOMBRE_A_TROUVER = 5
nombre_entre = int(input("Veuillez entrer un nombre: "), base=64)
print(nombre_entre)
while nombre_entre != NOMBRE_A_TROUVER:
    if nombre_entre > NOMBRE_A_TROUVER:
        print("c'est moins")
    else:
        print("c'est plus")
    nombre_entre = int(input("Veuillez entrer un nombre: "))
print("c'est fini")