from unittest import TestCase

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario
from objets_metiers.partie import Partie

class TestDaoOrganisateur(TestCase):

    def test_liste_joueurs(self):
        # GIVEN
        # WHEN
        res=DAO().liste_joueurs()
        #THEN
        self.assertIsInstance(res, list)
        