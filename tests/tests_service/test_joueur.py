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

    def test_changer_classde_perso(self):
