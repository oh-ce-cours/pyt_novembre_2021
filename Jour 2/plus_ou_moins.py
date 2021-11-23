def my_input():
    inputed = input("Veuillez entrer un nombre: ")
    res = None
    if inputed.isnumeric():
        res = int(inputed) 
    return res 

NOMBRE_A_TROUVER = 5
nombre_entre = my_input()
print(nombre_entre)
while nombre_entre != NOMBRE_A_TROUVER:
    if nombre_entre > NOMBRE_A_TROUVER:
        print("c'est moins")
    else:
        print("c'est plus")
    nombre_entre = my_input()
print("c'est fini")