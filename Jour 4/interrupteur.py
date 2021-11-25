class Interrupteur:
    def __init__(self, question_lieu, question_etat):
        self.question_lieu = question_lieu
        self.question_etat = question_etat

    def tourner(self):
        # if self.etat.isnumeric():
        if self.question_etat == 1:
            print(f"la lumiere > {self.question_lieu} < est allumé(e)")
        elif self.question_etat == 0:
            print(f"la lumiere > {self.question_lieu} < est éteinte")
        else:
            self.question_etat != 0 or self.question_etat != 1
            print("Veuillez actionner le bouton, l'état doit être en 0 et 1")


# test unitaire
interrupteursalon = Interrupteur("salon", 1)
interrupteursalon.tourner()
interrupteursalon = Interrupteur("salon", 0)
interrupteursalon.tourner()
interrupteursalon = Interrupteur("salon", 3)
interrupteursalon.tourner()
question_lieu = input(
    "indiquer le nom de l'interrupteur que vous souhaitez allumer >>> "
)
question_etat = input(
    'voulez vous allumer ou eteindre la lumiere, repondez par "allumer" ou "eteindre" à la question >>> '
)
question_etat = question_etat.lower()
question_etat = question_etat.strip()
if question_etat == "allumer":
    question_etat = 1
    question_etat = int(question_etat)
elif question_etat == "eteindre":
    question_etat = 0
    question_etat = int(question_etat)
else:
    print("veuillez indiquer eteindre ou allumer")
# print(question_lieu,type( question_lieu))
# print(question_etat, type(question_etat))
interrupteursalon = Interrupteur(question_lieu, question_etat)
interrupteursalon.tourner()
