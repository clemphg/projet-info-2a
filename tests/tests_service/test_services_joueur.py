import unittest
from unittest import TestCase

from service.service_joueur import ServiceJoueur

from objets_metiers.joueur import Joueur

from objets_metiers.personnage import Personnage

import hashlib

class TestServicePersonnage():

    def test_creer_personnage(self):
        # On donne un personnage valide
        perso=Personnage( id=None, nom="nom", age=1, race="race", niveau=1, classe="classe", pseudo_j="Hilaire100")
        # WHEN
        test=ServiceJoueur().creation_personnage(perso[0],perso)
        #THEN
        self.assertTrue(test)

    def test_changer_classe_perso(self):
        # On donne un personnage et une classe valide
        perso=Personnage( id=None, nom="nom", age=1, race="race", niveau=1, classe="classe", pseudo_j="Hilaire100")
        classe_a_tester="Barbare"
        # WHEN
        test=ServiceJoueur().changer_classe_perso(perso, classe_a_tester)
        #THEN
        self.assertTrue(test)

    def test_details_partie(self):
        # On donne un id partie valide
        id_patie=1
        # WHEN
        test=ServiceJoueur().details_partie(id_partie)
        #THEN
        self.assertTrue(test)

    def test_liste_parties(self):
        #On donne un pseudo joueur valide
        pseudo="Marielle90"
        # WHEN
        test=ServiceJoueur().liste_parties(pseudo)
        # THEN
        self.assertTrue(test)

    def test_desinscription_personnage_true(self):
        #On donne un id_perso et un id_partie valide
        id_perso=1
        id_partie=1
        # WHEN
        test=ServiceJoueur().desinscription_personnage(id_perso, id_partie)
        # THEN
        self.assertTrue(test)

    def test_desinscription_personnage_false(self):
        #On donne un id_perso et un id_partie qui ne correspondent pas un couple de inscription partie existant
        id_perso=1
        id_partie=3
        # WHEN
        test=ServiceJoueur().desinscription_personnage(id_perso, id_partie)
        # THEN
        self.assertTrue(test,"le personnage n'est pas inscrit à la partie")

    def test_liste_creneaux_dispos(self):
        #On donne un joueur valide
        joueur=Joueur('Hilaire100', 58)
        # WHEN
        test=ServiceJoueur().liste_creneaux_dispos(joueur)
        # THEN
        self.assertTrue(test)



