from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur

class TestDaoJoueur(TestCase):

    def test_creer_joueur(self):
        # GIVEN
        j = Joueur("riri",20)

        # WHEN
        DAO().cr

        #THEN


