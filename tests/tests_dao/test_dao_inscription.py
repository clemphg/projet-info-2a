from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur

import hashlib

class TestDaoJoueur(TestCase):

    def test_peudo_libre_true(self):
        # GIVEN
        pseudo_a_tester = "soleil"
        # WHEN
        test = DAO().verifier_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertTrue(test)

    def test_pseudo_libre_false(self):
        # GIVEN
        pseudo_a_tester = "Rebecca70"
        # WHEN
        test = DAO().verifier_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertFalse(test)



