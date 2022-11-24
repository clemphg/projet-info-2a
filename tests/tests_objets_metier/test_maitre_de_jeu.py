from unittest import TestCase

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario


class TestMaitreDeJeu(TestCase):

    def test_creer_scenario_possible(self):
        # GIVEN
        mj = MaitreDeJeu("riri",20)
        # WHEN
        status = mj.creer_scenario(1, "nom","scenario",5)
        # THEN
        self.assertTrue(status)

    def test_creer_scenario_impossible(self):
        # GIVEN
        mj = MaitreDeJeu("riri",20,[Scenario(nom="nom",description="hello",niveau_min=10),
                                    Scenario(nom="nom2",description="hello2",niveau_min=5)])
        # WHEN
        status = mj.creer_scenario(3, "nom3","description3",3)
        # THEN
        self.assertFalse(status)


