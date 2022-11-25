from unittest import TestCase

from dao.dao import DAO
from objets_metiers.organisateur import Organisateur
from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario
from objets_metiers.partie import Partie

class TestDaoOrganisateur(TestCase):

    def test_chercher_par_pseudo_org(self):
        # On donne un psuedo valide
        pseudo_val='Amima20'
        # WHEN
        test=DAO().chercher_par_pseudo_org(pseudo_val)
        result=Organisateur(pseudo_val)
        #THEN 
        self.assertEqual(result.pseudo,test.pseudo)
