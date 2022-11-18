from unittest import TestCase
from service.service_inscription_connexion import *
from objets_metiers.joueur import Joueur
import hashlib

class TestServiceJoueur(TestCase):

    def test_peudo_libre(self):
        # GIVEN
        pseudo_a_tester = "soleil"
        # WHEN
        test = ServiceInscriptionConnexion().test_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertTrue(test)

    def test_pseudo_libre():
        # GIVEN
        pseudo_a_tester = "Rebecca70" 
        # WHEN
        test = ServiceInscriptionConnexion().test_pseudo_libre(pseudo_a_tester)
        #THEN
        self.assertTrue(test,"Le pseudo est deja prit")

    def test_mdp(self):
        # GIVEN
        mdp_a_tester = "Armandblabla34!"
        pseudo_a_tester="Rebecca70"
        # WHEN
        test = ServiceInscriptionConnexion().verifier_mdp_correct(pseudo_a_tester,mdp_a_tester)
        #THEN
        self.assertTrue(test)
    
    def test_mdp(self):
        # GIVEN
        mdp_a_tester = "Amandblabla34!"
        pseudo_a_tester="Rebecca70"
        # WHEN
        test = ServiceInscriptionConnexion().verifier_mdp_correct(pseudo_a_tester,mdp_a_tester)
        #THEN
        self.assertTrue(test,"Le mot de passe est incorrect")

    def test_creation_joueur(self):
        # GIVEN
        mdp_a_tester = "Bonjour123!"
        pseudo_a_tester="dragon04"
        type_a_tester="Joueur"
        age_a_tester=23
        # WHEN
        test = ServiceInscriptionConnexion().creer_utilisateur(pseudo_a_tester,age_a_tester,mdp_a_tester,type_a_tester)
        #THEN
        self.assertTrue(test)
        
        def test_instancier_utilisateur(self):
            # GIVEN
            pseudo_a_tester="Aimee20"
            type_a_tester="Joueur"
          
            # WHEN
            test = ServiceInscriptionConnexion().instancier_utilisateur(pseudo_a_tester,type_a_tester)
            #THEN
            self.assertTrue(test)
