from unittest import TestCase

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario
from objets_metiers.partie import Partie

class TestDaoMaitreDeJeu(TestCase):

    def test_creer_mj(self):
        # GIVEN
        # On donne un couple Joueur, mdp valide
        mj=MaitreDeJeu("Westbric",34)
        mdp="Peutofeu8**"
        # WHEN
        test=DAO().creer_mj(mj,mdp)
        #THEN
        self.assertTrue(test)

    def test_creer_scenario(self):
        # GIVEN
        scenario=Scenario(id=None, nom="le donjon",description="une expérience dans un donjon rempli de monstres", niveau_min=20, pseudo_mj="Westbric")
        # WHEN
        res=DAO().creer_scenario(scenario)
        #THEN
        self.assertIsInstance(res, int)

    def test_creer_partie(self):
        # GIVEN
        partie=Partie(id=None, creneau=2,
                      scenario=Scenario(id=None,
                                        nom="le donjon",
                                        description="une expérience dans un donjon rempli de monstres",
                                        niveau_min=20,
                                        pseudo_mj="Westbric"))
        # WHEN
        res=DAO().creer_partie(partie)
        #THEN
        self.assertIsInstance(res, int)

    def test_chercher_par_pseudo_mj(self):
        # GIVEN
        mj=MaitreDeJeu("Marie18",28)
        # WHEN
        result=DAO().chercher_par_pseudo_mj("Marie18")
        #THEN
        testpseudo = (mj.pseudo == result.pseudo)
        testage = (mj.age == result.age)
        self.assertTrue(testpseudo and testage)
