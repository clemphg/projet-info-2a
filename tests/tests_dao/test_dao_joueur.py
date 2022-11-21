from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur

class TestDaoJoueur(TestCase):
    """
    def test_creer_joueur(self):
        # GIVEN
        # On donne un couple Joueur, mdp valide
        j=Joueur("Westbric00",34)
        mdp="Peutofeu8**"
        # WHEN
        test=DAO().creer_joueur(j,mdp)
        #THEN
        self.assertTrue(test)
    """

    def test_chercher_par_pseudo_j(self):
        # GIVEN
        j=Joueur("Rebecca70",24)
        # WHEN
        result=DAO().chercher_par_pseudo_j("Rebecca70")
        #THEN
        testpseudo = (j.pseudo == result.pseudo)
        testage = (j.age == result.age)
        self.assertTrue(testpseudo and testage)




