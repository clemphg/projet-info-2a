from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur
from objets_metiers.personnage import Personnage
class TestDaoJoueur(TestCase):

    def test_creer_joueur(self):
        # GIVEN
        # On donne un couple Joueur, mdp valide
        j=Joueur("Westbric00",34)
        mdp="Peutofeu8**"
        # WHEN
        test=DAO().creer_joueur(j,mdp)
        #THEN
        self.assertTrue(test)

    def test_creer_perso(self):
        # GIVEN
        perso = Personnage(id=None, nom="Fafnir", age=135, race="Dwarf", niveau=50, classe="Ranger", pseudo_j="Westbric00")
        # WHEN
        res=DAO().creer_perso(perso)
        #THEN
        self.assertIsInstance(res, int)

    def test_chercher_par_pseudo_j(self):
        # GIVEN
        j=Joueur("Rebecca70",24)
        # WHEN
        result=DAO().chercher_par_pseudo_j("Rebecca70")
        #THEN
        testpseudo = (j.pseudo == result.pseudo)
        testage = (j.age == result.age)
        self.assertTrue(testpseudo and testage)

    def test_chercher_par_id_perso(self):
        # GIVEN
        id_perso=1
        # WHEN
        res=DAO().chercher_par_id_perso(id_perso)
        #THEN
        self.assertIsInstance(res, Personnage)

    def test_inscription_personnage(self):
        # GIVEN
        id_perso = 1
        id_partie = 2
        # WHEN
        res=DAO().inscription_personnage(id_perso, id_partie)
        # THEN
        self.assertTrue(res)


