class Personne:
    def __init__(self, nom, naissance):
        self.naissance = naissance
        self.age = annee_en_cours - naissance

    def est_majeur(self):
        age_majorite = 18
        return self.age > age_majorite
