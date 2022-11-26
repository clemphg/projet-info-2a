from unittest import TestCase

from dao.dao import DAO

from objets_metiers.scenario import Scenario

class TestDaoScenario(TestCase):

    def test_creer_scenario(self):
        # On donne un scneario valide
        scena=Scenario(id=None,
                       nom="Terreur_nocture",
                       description="Les actions de nuits seront mis en avant et les degats de nuit seront décuplés ",
                       niveau_min=50,
                       pseudo_mj="Amy10")
        # WHEN
        res=DAO().creer_scenario(scena)
        #THEN
        self.assertIsInstance(res, int)

    def test_supprimer_scenario(self):
        #On donne un scenario a supprimer
        scena=Scenario(8,'Sauver la princesse', 'Le but est de sauver la princesse Emily mais attention aux ogres', 80,'Hil100')
        # WHEN
        test=DAO().supprimer_scenario(scena)
        #THEN
        self.assertTrue(test)

