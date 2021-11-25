from interrupteur import Interrupteur


def my_interrupteur():
    return Interrupteur("chambre", 0)


def test_creation_interrupteur(my_interrupteur):
    assert i.etat == 0
    i.actionner_bouton(1)
    assert i.etat == 1


def test_creation_interrupteur_2(my_interrupteur):
    assert i.etat == 1
    i.actionner_bouton(10)
    assert i.etat == 10
