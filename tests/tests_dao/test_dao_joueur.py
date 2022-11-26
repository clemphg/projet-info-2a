from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur
from objets_metiers.personnage import Personnage

class TestDaoJoueur(TestCase):

    def test_liste_joueur(self):
        #WHEN
        test=DAO().liste_joueurs()
        #THEN
        self.assertEqual(len(test),5)
        self.assertIsInstance(test[1],Joueur)

    def test_creer_joueur(self):
        # GIVEN
        # On donne un couple Joueur, mdp valide
        j=Joueur("Westbric00",34)
        mdp="Peutofeu8**"
        # WHEN
        test=DAO().creer_joueur(j,mdp)
        #THEN
        self.assertTrue(test)

    def test_chercher_par_pseudo_j(self):
        # GIVEN
        pseudo = "Rebecca70"
        age = 24
        persos = [Personnage(1,'Elyanna', 200,'Elf',200, 'Wizard','Rebecca70'),
                  Personnage(2,'Emir', 18, 'Human',200,'Rogue','Rebecca70'),
                  Personnage(3,'Elliot', 500, 'Tiefling',200,'Bard','Rebecca70')]
        j = Joueur(pseudo, age, persos)
        # WHEN
        res=DAO().chercher_par_pseudo_j(pseudo)
        #THEN
        self.assertEqual(j.pseudo,res.pseudo)
        self.assertEqual(j.age,res.age)
        self.assertEqual(len(j.personnages),len(res.personnages))

    def test_liste_inscription_joueur(self):
        #GIVEN
        pseudo = "Rebecca70"
        #WHEN
        test=DAO().liste_inscriptions_joueur(pseudo)
        #THEN
        self.assertIsInstance(test[1],dict)








