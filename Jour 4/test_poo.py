from poo import Personne
import pytest


@pytest.fixture
def matthieu():
    return Personne(naissance=1990, nom="Matthieu")


@pytest.fixture
def paul():
    return Personne(naissance=1990, nom="Matthieu")


def test_creation_personne(p1):
    p1 = Personne(naissance=1990, nom="Matthieu")
    p2 = Personne("Paul", 2020)

    assert p1.est_majeur()
    assert not p2.est_majeur()


def test_presentation():
    p1 = Personne(naissance=1990, nom="Matthieu")
    assert "Matthieu" in str(p1)
    assert "1990" in str(p1)
