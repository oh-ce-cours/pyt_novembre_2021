from poo import Personne
import pytest


@pytest.fixture
def matthieu():
    return Personne(naissance=1990, nom="Matthieu")


@pytest.fixture
def paul():
    return Personne("Paul", 2020)


def test_creation_personne(matthieu, paul):
    assert matthieu.est_majeur()
    assert not paul.est_majeur()


def test_presentation(matthieu):
    assert "Matthieu" in str(matthieu)
    assert "1990" in str(matthieu)


def test_change_age_majorite(matthieu, paul):
    Personne.AGE_MAJORITE = 40
    assert not matthieu.est_majeur()
    assert not paul.est_majeur()
