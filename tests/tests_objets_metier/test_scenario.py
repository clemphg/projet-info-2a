from unittest import TestCase
import unittest

from objets_metiers.scenario import Scenario


class TestScenario(TestCase):

    def test_id(self):
        # GIVEN
        identifiant =19
        # WHEN
        scenario = Scenario(id=identifiant,nom="scenar1",description="Une grande aventure",niveau_min=3)
        # THEN
        self.assertEqual(identifiant,scenario.id)

    def test_id_setter(self):
        # GIVEN
        scenario = Scenario(id=19,nom="scenar1",description="Une grande aventure",niveau_min=3)
        nv_id = 14
        # WHEN
        scenario.id = nv_id
        # THEN
        self.assertEqual(nv_id,scenario.id)

    def test_nom(self):
        # GIVEN
        nom = "A l aventure"
        # WHEN
        scenario = Scenario(nom=nom,description="Une grande aventure",niveau_min=3)
        # THEN
        self.assertEqual(nom,scenario.nom)

    def test_description(self):
        # GIVEN
        description = "Une immense aventure"
        # WHEN
        scenario = Scenario(nom="scenar1",description=description,niveau_min=3)
        # THEN
        self.assertEqual(description,scenario.description)

    def test_niveau_min(self):
        # GIVEN
        niveau = 7
        # WHEN
        scenario = Scenario(nom="scenar1",description="Une grande aventure",niveau_min=niveau)
        # THEN
        self.assertEqual(niveau,scenario.niveau_min)
