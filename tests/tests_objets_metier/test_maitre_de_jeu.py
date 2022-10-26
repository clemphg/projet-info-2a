from unittest import TestCase
import unittest

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario


class TestMaitreDeJeu(TestCase):

    def test_creer_scenario_possible(self):
        # GIVEN
        mj = MaitreDeJeu("riri",20)
        # WHEN
        status = mj.creer_scenario("nom","scenario",5)
        # THEN
        self.assertTrue(status)

    def test_creer_scenario_impossible(self):
        # GIVEN
        mj = MaitreDeJeu("riri",20,[Scenario(nom="nom",description="hello",niveau_min=10),
                                    Scenario(nom="nom2",description="hello2",niveau_min=5)])
        # WHEN
        status = mj.creer_scenario("nom3","description3",3)
        # THEN
        self.assertFalse(status)

    def test_nom(self):
        # GIVEN
        pseudo = "riri"
        # WHEN
        mj = MaitreDeJeu(pseudo,20)
        # THEN
        self.assertEqual(pseudo, mj.pseudo)

    def test_age(self):
        # GIVEN
        age = 16
        # WHEN
        mj = MaitreDeJeu("riri",age)
        # THEN
        self.assertEqual(age, mj.age)

    def test_scenarios(self):
        # GIVEN
        scenarios = [Scenario(nom="nom",description="hello",niveau_min=10),
                     Scenario(nom="nom2",description="hello2",niveau_min=5)]
        # WHEN
        mj = MaitreDeJeu("riri",20,scenarios)
        # THEN
        self.assertEqual(scenarios, mj.scenarios)


