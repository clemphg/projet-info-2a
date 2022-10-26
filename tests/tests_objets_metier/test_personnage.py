from unittest import TestCase
import unittest

from objets_metiers.personnage import Personnage


class TestPersonnage(TestCase):

    def test_id(self):
        # GIVEN
        identifiant =19
        # WHEN
        perso = Personnage(id=identifiant,nom="fifi",age=15,race="Elf",niveau=12,classe="Wizard")
        # THEN
        self.assertEqual(identifiant,perso.id)

    def test_id_setter(self):
        # GIVEN
        perso = Personnage(id=19,nom="fifi",age=15,race="Elf",niveau=12,classe="Wizard")
        nv_id = 14
        # WHEN
        perso.id = nv_id
        # THEN
        self.assertEqual(nv_id,perso.id)

    def test_nom(self):
        # GIVEN
        prenom = "fifi"
        # WHEN
        perso = Personnage(nom=prenom,age=15,race="Elf",niveau=12,classe="Wizard")
        # THEN
        self.assertEqual(prenom,perso.nom)

    def test_race(self):
        # GIVEN
        race = "Gnome"
        # WHEN
        perso = Personnage(nom="fifi",age=15,race=race,niveau=12,classe="Wizard")
        # THEN
        self.assertEqual(race,perso.race)

    def test_classe(self):
        # GIVEN
        classe = "Wizard"
        # WHEN
        perso = Personnage(nom="fifi",age=15,race="Gnome",niveau=12,classe=classe)
        # THEN
        self.assertEqual(classe,perso.classe)

    def test_classe_setter(self):
        # GIVEN
        perso = Personnage(nom="fifi",age=15,race="Elf",niveau=12,classe="Wizard")
        nvlle_classe = "Warlock"
        # WHEN
        perso.classe = nvlle_classe
        # THEN
        self.assertEqual(perso.classe,nvlle_classe)