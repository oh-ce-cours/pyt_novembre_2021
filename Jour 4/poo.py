class Personne:
    def __init__(self, nom, naissance):
        annee_en_cours = 2021
        self.naissance = naissance
        self.age = annee_en_cours - naissance

    def est_majeur(self):
        age_majorite = 18
        return self.age > age_majorite
