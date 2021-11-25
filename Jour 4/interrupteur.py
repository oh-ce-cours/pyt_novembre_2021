class Interrupteur:
    def __init__(self, question_lieu, etat):
        self.question_lieu = question_lieu
        self.etat = etat

    def afficher_etat(self):
        if self.etat == 1:
            print(f"la lumiere > {self.question_lieu} < est allumé(e)")
        elif self.etat == 0:
            print(f"la lumiere > {self.question_lieu} < est éteinte")
        else:
            self.etat != 0 or self.etat != 1
            print("Veuillez actionner le bouton, l'état doit être en 0 et 1")

    def actionner_bouton(self, etat_voulu):
        self.etat = etat_voulu
        res = (
            f"Je m'appelle {nom} né en {naissance} (age={age}) ; "
            f"majeur={est_majeur}"
        )


def main():
    interrupteursalon = Interrupteur("salon", 1)
    interrupteursalon.afficher_etat()
    interrupteursalon = Interrupteur("salon", 0)
    interrupteursalon.afficher_etat()
    interrupteursalon = Interrupteur("salon", 3)
    interrupteursalon.afficher_etat()
    question_lieu = input(
        "indiquer le nom de l'interrupteur que vous souhaitez allumer >>> "
    )
    question_etat = input(
        'voulez vous allumer ou eteindre la lumiere, repondez par "allumer" ou "eteindre" à la question >>> '
    )
    question_etat = question_etat.lower().strip()

    etat = 0
    if question_etat == "allumer":
        etat = 1
    elif question_etat == "eteindre":
        etat = 0
    else:
        print("veuillez indiquer eteindre ou allumer")
    # print(question_lieu,type( question_lieu))
    # print(question_etat, type(question_etat))
    interrupteursalon = Interrupteur(question_lieu, etat)
    interrupteursalon.afficher_etat()
    interrupteursalon.etat = 13432
    interrupteursalon.afficher_etat()
    print(dir(interrupteursalon))


if __name__ == "__main__":
    main()
