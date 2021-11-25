from interrupteur import Interrupteur


def my_interrupteur():
    return Interrupteur("chambre", 0)


def test_creation_interrupteur(my_interrupteur):
    assert my_interrupteur.etat == 0
    my_interrupteur.actionner_bouton(1)
    assert my_interrupteur.etat == 1


def test_creation_interrupteur_2(my_interrupteur):
    assert my_interrupteur.etat == 1
    my_interrupteur.actionner_bouton(10)
    assert my_interrupteur.etat == 10
