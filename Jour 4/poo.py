class Personne:
    AGE_MAJORITE = 18
    NB_PERSONNES_CREES = 0

    @staticmethod
    def calcule_age(naissance):
        annee_en_cours = 2021
        return annee_en_cours - naissance

    def __init__(self, nom, naissance):
        type(self).NB_PERSONNES_CREES += 1
        self.naissance = naissance
        self.age = self.calcule_age(naissance)
        self.nom = nom

    def est_majeur(self):
        return self.age > self.AGE_MAJORITE

    def __str__(self):
        return f"Je suis {self.nom} et je suis né en {self.naissance}"

    @classmethod
    def creer(cls):
        cls.AGE_MAJORITE += 1
        return cls("clone", 2021)

    def __del__(self):
        print(self, "est supprimé")
        type(self).NB_PERSONNES_CREES -= 1


if __name__ == "__main__":
    print(Personne.creer())
    print(Personne.NB_PERSONNES_CREES)
    print(Personne.creer())
    print(Personne.NB_PERSONNES_CREES)
    print(Personne.creer())
    print(Personne.NB_PERSONNES_CREES)

    p1 = Personne(1, 2)
    print(Personne.NB_PERSONNES_CREES)
