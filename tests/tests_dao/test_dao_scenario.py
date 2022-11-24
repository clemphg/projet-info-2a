from unittest import TestCase

from dao.dao import DAO

from objets_metiers.scenario import Scenario

class TestDaoScenario(TestCase):

    def test_creer_scenario(self):
        # On donne un scneario valide
        scena=Scenario("Terreur_nocture","Les actions de nuits seront mis en avant et les degats de nuit seront décuplés ",50,"Amy10")
        # WHEN
        tets=DAO().creer_scenario(scena)
        #THEN
        self.assertTrue(test)
        pass

