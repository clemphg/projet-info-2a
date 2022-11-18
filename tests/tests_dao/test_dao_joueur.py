from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur

class TestDaoJoueur(TestCase):

    def test_creer_joueur(self):
        # On donne un couple Joueur, mdp valide
        perso=[Joueur("Westbric00",34),Peutofeu8**]
        # WHEN
        tets=DAO().creer_joueur(perso[0],perso[1])
        #THEN
        self.assertTrue(test)
        pass

    def test_chercher_par_pseudo_j(self):
         # On donne un psuedo valide
        pseudo_val="Westbric00"
        # WHEN
        test=DAO().chercher_par_pseudo_j(pseudo_val)
        result=Joueur("Westbric00",34,[])
        result[2].sort(key=lambda result[2]:result[2].id_perso)
        test[2].sort(key=lambda test[2]:test[2].id_perso)
        #THEN 
        self.assertEqual(result,test)
        pass




    