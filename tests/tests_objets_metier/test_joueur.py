from unittest import TestCase

from objets_metiers.joueur import Joueur
from objets_metiers.personnage import Personnage


class TestJoueur(TestCase):

    def test_creer_personnage_possible(self):
        # GIVEN
        joueur = Joueur("riri",20)
        # WHEN
        status = joueur.creer_personnage(1, "fifi", 234, "Elf", 3, "Warrior")
        # THEN
        self.assertTrue(status)

    def test_creer_personnage_impossible(self):
        # GIVEN
        joueur = Joueur("riri",20,[Personnage("A"),
                                   Personnage("B"),
                                   Personnage("C")])
        # WHEN
        status = joueur.creer_personnage(4, "fifi", 234, "Elf", 3, "Warrior")
        # THEN
        self.assertFalse(status)

    def test_pseudo(self):
        # GIVEN
        pseudo = "riri"
        # WHEN
        joueur = Joueur(pseudo,20)
        # THEN
        self.assertEqual(pseudo, joueur.pseudo)

    def test_age(self):
        # GIVEN
        age = 20
        # WHEN
        joueur = Joueur("riri",age)
        # THEN
        self.assertEqual(age, joueur.age)

    def test_personnages(self):
        # GIVEN
        personnages = [Personnage("A"),
                       Personnage("B")]
        # WHEN
        joueur = Joueur("riri",20,personnages)
        # THEN
        self.assertEqual(personnages, joueur.personnages)
