import pytest
from interrupteur import Interrupteur


@pytest.fixture
def interrupteur_salon_eteind():
    return Interrupteur("salon", 0)


@pytest.fixture
def interrupteur_salon_allume():
    return Interrupteur("salon", 1)


def test_creation_interrupteur(interrupteur_salon_eteind):
    assert interrupteur_salon_eteind.etat == 0
    interrupteur_salon_eteind.actionner_bouton(1)
    assert interrupteur_salon_eteind.etat == 1


def test_creation_interrupteur_2(interrupteur_salon_allume):
    interrupteur_salon_allume.actionner_bouton(10)
    assert interrupteur_salon_allume.etat == 10
