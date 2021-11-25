from interrupteur import Interrupteur


def test_creation_interrupteur():
    i = Interrupteur("chambre", 0)
    assert i.etat == 0
    i.actionner_bouton(1)
    assert i.etat == 1


def test_creation_interrupteur_2():
    i = Interrupteur("chambre", 0)
    assert i.etat == 0
    i.actionner_bouton(1)
    assert i.etat == 1
