class Interrupteur:
    def __init__(self, questionlieu, questionetat):
        self.questionlieu = questionlieu
        self.questionetat = questionetat

    def tourner(self):
        # if self.etat.isnumeric():
        if self.questionetat == 1:
            print(f"la lumiere > {self.questionlieu} < est allumé(e)")
        elif self.questionetat == 0:
            print(f"la lumiere > {self.questionlieu} < est éteinte")
        else:
            self.questionetat != 0 or self.questionetat != 1
            print("Veuillez actionner le bouton, l'état doit être en 0 et 1")


# test unitaire
interrupteursalon = Interrupteur("salon", 1)
interrupteursalon.tourner()
interrupteursalon = Interrupteur("salon", 0)
interrupteursalon.tourner()
interrupteursalon = Interrupteur("salon", 3)
interrupteursalon.tourner()
questionlieu = input(
    "indiquer le nom de l'interrupteur que vous souhaitez allumer >>> "
)
questionetat = input(
    'voulez vous allumer ou eteindre la lumiere, repondez par "allumer" ou "eteindre" à la question >>> '
)
questionetat = questionetat.lower()
questionetat = questionetat.strip()
if questionetat == "allumer":
    questionetat = 1
    questionetat = int(questionetat)
elif questionetat == "eteindre":
    questionetat = 0
    questionetat = int(questionetat)
else:
    print("veuillez indiquer eteindre ou allumer")
# print(questionlieu,type( questionlieu))
# print(questionetat, type(questionetat))
interrupteursalon = Interrupteur(questionlieu, questionetat)
interrupteursalon.tourner()
