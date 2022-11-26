from unittest import TestCase

from dao.dao import DAO

from objets_metiers.scenario import Scenario

class TestDaoScenario(TestCase):

    def test_creer_scenario(self):
        # On donne un scneario valide
        scena=Scenario(id=None,"Terreur_nocture","Les actions de nuits seront mis en avant et les degats de nuit seront décuplés ",50,"Amy10")
        # WHEN
        tets=DAO().creer_scenario(scena)
        #THEN
        self.assertTrue(test)
    
    def test_supprimer_scenario(self):
        #On donne un scenario a supprimer
        scena=Scenario(8,'Sauver la princesse', 'Le but est de sauver la princesse Emily mais attention aux ogres', 80,'Hil100')
        # WHEN
        tets=DAO().supprimer_scenario(scena)
        #THEN
        self.assertTrue(test)

