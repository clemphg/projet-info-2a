from unittest import TestCase

from service.service_joueur import ServiceJoueur

from objets_metiers.joueur import Joueur

from objets_metiers.personnage import Personnage


class TestServiceJoueur(TestCase):

    def test_creation_personnage(self):
        # GIVEN
        perso=Personnage( id=None, nom="nom", age=1, race="race", niveau=1, classe="classe", pseudo_j="Hilaire100")
        # WHEN
        res=ServiceJoueur().creation_personnage(perso)
        #THEN
        self.assertIsInstance(res,int)

    def test_changer_classe_perso(self):
        # GIVEN
        perso=Personnage(id=1, nom="Elyanna", age=200, race="elf", niveau=200, classe="enchanteresse", pseudo_j="Rebecca70")
        nvlle_classe="Barbare"
        # WHEN
        test=ServiceJoueur().changer_classe_perso(perso, nvlle_classe=nvlle_classe)
        #THEN
        self.assertTrue(test)

    def test_details_partie(self):
        # On donne un id partie valide
        id_partie=1
        # WHEN
        test=ServiceJoueur().details_partie(id_partie)
        #THEN
        self.assertIsNotNone(test)

    def test_liste_parties(self):
        # GIVEN
        #On donne un pseudo joueur valide
        pseudo="Marielle90"
        # WHEN
        res=ServiceJoueur().liste_parties(pseudo)
        # THEN
        self.assertIsInstance(res, list)

    def test_desinscription_personnage_true(self):
        # GIVEN
        #On donne un id_perso et un id_partie valide
        id_perso=1
        id_partie=1
        pseudo_j = "Rebecca70"
        # WHEN
        test=ServiceJoueur().desinscription_personnage(id_perso, id_partie, pseudo_j)
        # THEN
        self.assertTrue(test)

    def test_inscription_perso_true(self):
        # GIVEN
        #On donne un id_perso et un id_partie valide
        id_perso=1
        id_partie=1
        pseudo_j = "Rebecca70"
        # WHEN
        test=ServiceJoueur().inscription_perso(id_perso, id_partie, pseudo_j)
        # THEN
        self.assertTrue(test)

    def test_desinscription_personnage_false(self):
        # GIVEN
        #On donne un id_perso et un id_partie qui ne correspondent pas un couple de inscription partie existant
        id_perso=1
        id_partie=3
        pseudo_j="Rebecca70"
        # WHEN
        test=ServiceJoueur().desinscription_personnage(id_perso, id_partie, pseudo_j)
        # THEN
        self.assertFalse(test)

    def test_liste_creneaux_dispos(self):
        #On donne un joueur valide
        joueur=Joueur('Hilaire100', 58)
        # WHEN
        test=ServiceJoueur().liste_creneaux_dispos(joueur)
        # THEN
        self.assertIsInstance(test, list)



