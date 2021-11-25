from poo import Personne


def test_creation_personne():
    p1 = Personne(naissance=1990, nom="Matthieu")
    p2 = Personne("Paul", 2020)
