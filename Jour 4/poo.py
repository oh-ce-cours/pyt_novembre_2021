class Personne:
    AGE_MAJORITE = 18

    def __init__(self, nom, naissance):
        annee_en_cours = 2021
        self.naissance = naissance
        self.age = annee_en_cours - naissance
        self.nom = nom

    def est_majeur(self):
        return self.age > self.AGE_MAJORITE

    def __str__(self):
        return f"Je suis {self.nom} et je suis né en {self.naissance}"

    @classmethod
    def creer(cls):
        return cls("clone", 2021)


if __name__ == "__main__":
    Personne.creer()
