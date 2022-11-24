from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur

import hashlib

class TestDaoInscription(TestCase):

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

    def test_verifier_mdp_correct_true(self):
        # GIVEN
        pseudo = "Aimee20"
        mdp= "Hebertblublu20?"
        mdp_a_tester = hashlib.sha256(pseudo.encode() + mdp.encode()).hexdigest()
        # WHEN
        res = DAO().verifier_mdp(pseudo, mdp_a_tester)
        # THEN
        self.assertTrue(res)

    def test_verifier_mdp_correct_false(self):
        # GIVEN
        pseudo = "Aimee20"
        mdp_a_tester = "faux_mdp?"
        # WHEN
        res = DAO().verifier_mdp(pseudo, mdp_a_tester)
        # THEN
        self.assertFalse(res)



