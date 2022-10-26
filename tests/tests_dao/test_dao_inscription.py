from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur

import hashlib

class TestDaoJoueur(TestCase):

    def test_peudo_libre(self):
        # GIVEN
        pseudo_a_tester = "soleil"
        # WHEN
        test = DAO().test_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertTrue(test)

