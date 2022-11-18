from unittest import TestCase

from service.service_joueur import *

from objets_metiers.joueur import Joueur

from objets_metiers.personnage import *

import hashlib

class TestServicePersonnage():

    def test_creer_personnage(self):
        # On donne un personnage valide
        perso=Personnage( id=None, nom="nom", age=1, race="race", niveau=1, classe="classe", pseudo_j="Hilaire100")
        # WHEN
        test=Service_Joueur().creation_personnage(perso[0],perso)
        #THEN
        self.assertTrue(test)

    def test_changer_classe_perso(self):
        # On donne un personnage et une classe valide
        perso=Personnage( id=None, nom="nom", age=1, race="race", niveau=1, classe="classe", pseudo_j="Hilaire100")
        classe_a_tester="Barbare"
        # WHEN
        test=Service_Joueur().changer_classe_perso(perso, classe_a_tester)
        #THEN
        self.assertTrue(test)
    
    def test_details_partie(self):
        # On donne un id partie valide
        id_patie=1
        # WHEN
        test=Service_Joueur().details_partie(id_partie)
        #THEN
        self.assertTrue(test)
    
    


