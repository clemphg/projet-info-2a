from unittest import TestCase

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario

class TestDaoMaitredejeu(TestCase):


    def test_liste_mjs(self):
        # WHEN
        test=DAO().liste_mjs()
        #THEN
        self.assertEqual(len(test),5)
        self.assertIsInstance(test[1],MaitreDeJeu)


    def test_creer_mj(self):
        # GIVEN
        mj=MaitreDeJeu("Brich52",34)
        mdp="Brandito62*"
        # WHEN
        test=DAO().creer_mj(mj, mdp)
        #THEN
        self.assertTrue(test)

    def test_chercher_par_pseudo_mj(self):
        # GIVEN
        pseudo="GiGigigi"
        age = 25
        scenarios = [Scenario(1,'Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGigigi'),
                     Scenario(2,'Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGigigi')]
        mj = MaitreDeJeu(pseudo, age, scenarios)
        # WHEN
        res=DAO().chercher_par_pseudo_mj(pseudo)
        #THEN
        self.assertEqual(mj.pseudo,res.pseudo)
        self.assertEqual(mj.age,res.age)
        self.assertEqual(len(mj.scenarios),len(res.scenarios))





