def est_divisible_par_3(nombre):
    return nombre % 3 == 0

def est_divisible_par_5(nombre):
    return nombre % 5 == 0

def regle_fizz_buzz(nombre):
    resultat = ""
    if est_divisible_par_3(nombre):
        resultat = resultat + "fizz"
    if est_divisible_par_5(nombre):
        resultat += "buzz"
    if not resultat :
        resultat = nombre
    return resultat
        
# for nombre in range(1, 101):
#     print(regle_fizz_buzz(nombre))

print(regle_fizz_buzz(3) == "fizz")
print(regle_fizz_buzz(5) == "buzz")
print(regle_fizz_buzz(15) == "fizzbuzz")
print(regle_fizz_buzz(2) == 2)