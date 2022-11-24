import unittest
from unittest import TestCase
from service.service_inscription_connexion import ServiceInscriptionConnexion
from objets_metiers.joueur import Joueur

class TestServiceInscriptionConnexion(TestCase):

    def test_verifier_peudo_libre_true(self):
        # GIVEN
        pseudo_a_tester = "soleil"
        # WHEN
        test = ServiceInscriptionConnexion().verifier_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertTrue(test)

    def test_verifier_peudo_libre_false(self):
        # GIVEN
        pseudo_a_tester = "Amy10"
        # WHEN
        test = ServiceInscriptionConnexion().verifier_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertFalse(test)

    def test_verifier_mdp_correct_true(self):
        # GIVEN
        pseudo = "Amy10"
        mdp_a_tester = "!!Heb2000"
        # WHEN
        test = ServiceInscriptionConnexion().verifier_mdp_correct(pseudo, mdp_a_tester)
        #THEN
        self.assertTrue(test)

    def test_verifier_mdp_correct_false(self):
        # GIVEN
        pseudo = "Amy10"
        mdp_a_tester = "faux"
        # WHEN
        test = ServiceInscriptionConnexion().verifier_mdp_correct(pseudo, mdp_a_tester)
        #THEN
        self.assertFalse(test)

    """
    def test_creer_utilisateur(self):
        # GIVEN
        pseudo = "NewGameMaster"
        age = 54
        mdp = "MotDePasse234:)"
        type_de_profil = "Maître de jeu"
        # WHEN
        res = ServiceInscriptionConnexion().creer_utilisateur(pseudo, age, mdp, type_de_profil)
        # THEN
        self.assertTrue(res)
    """

    def test_instancier_utilisateur_ok(self):
        # GIVEN
        pseudo = "Hilaire100"
        type_de_profil = "Joueur"
        # WHEN
        res = ServiceInscriptionConnexion().instancier_utilisateur(pseudo, type_de_profil)
        # THEN
        self.assertIsNotNone(res)

    def test_instancier_utilisateur_pas_ok(self):
        # GIVEN
        pseudo = "test"
        type_de_profil = "Organisateur"
        # WHEN
        res = ServiceInscriptionConnexion().instancier_utilisateur(pseudo, type_de_profil)
        # THEN
        self.assertIsNone(res)