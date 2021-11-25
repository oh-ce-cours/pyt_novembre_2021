from poo import Personne


def test_creation_personne():
    p1 = Personne(naissance=1990, nom="Matthieu")
    p2 = Personne("Paul", 2020)

    assert p1.est_majeur()
    assert not p2.est_majeur()


def test_presentation():
    p1 = Personne(naissance=1990, nom="Matthieu")
    print(p1)  # Je suis Matthieu né en 1990
    assert "Matthieu" in str(p1)
