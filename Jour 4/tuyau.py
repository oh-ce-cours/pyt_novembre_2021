class Tuyau:
    def __init__(self, geometrie):
        pass

    @staticmethod
    def traitement_fichier_ascii(fichier_de_geometrie):
        ...
        return geometrie

    @staticmethod
    def traitement_fichier_binaire(fichier_de_geometrie):
        ...
        return geometrie

    @classmethod
    def load_from_fichier_type_ascii(cls, fichier):
        geometrie = traitement_fichier_ascii(fichier)
        return cls(geometrie)

    @classmethod
    def load_from_fichier_type_binaire(cls, fichier):
        geometrie = traitement_fichier_binaire(fichier)
        return cls(geometrie)

    @classmethod
    def load_from_fichier(cls, fichier):
        if type_fichier == "binaire":
            tuyau = cls.load_from_fichier_type_binaire(fichier)
        elif type_fichier == "ascii":
            tuyau = cls.load_from_fichier_type_ascii(fichier)

        return tuyau


tuyau = Tuyau.load_from_fichier("/tmp/....")
tuyau.compute()
