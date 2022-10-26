from unittest import TestCase
import unittest

from objets_metiers.personnage import Personnage


class TestPersonnage(TestCase):

    def test_modifier_classe(self):
        # GIVEN
        perso = Personnage(nom="fifi",age=15,race="Elf",niveau=12,classe="Wizard")
        nvlle_classe = "Warlock"
        # WHEN
        perso.modifier_classe(nvlle_classe)
        # THEN
        self.assertEqual(perso.classe,nvlle_classe)

    def test_nom(self):
        # GIVEN
        prenom = "fifi"
        # WHEN
        perso = Personnage(nom=prenom,age=15,race="Elf",niveau=12,classe="Wizard")
        # THEN
        self.assertEqual(prenom,perso.nom)