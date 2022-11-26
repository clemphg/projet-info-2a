from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur
from objets_metiers.personnage import Personnage

class TestDaoJoueur(TestCase):

    def test_liste_joueur(self):
        #WHEN
        test=DAO().liste_joueurs()
        #THEN 
        self.assertEqual(len(test),4)
        self.assertIsInstance(test[1],Joueur)
        pass
        

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
        # On donne un psuedo valide
        pseudo_val="Rebecca70"
        # WHEN
        test=DAO().chercher_par_pseudo_j(pseudo_val)
        result=Joueur("Rebecca70",24, [Personnage(1,'Elyanna', 200,'elf',200, 'enchantresse','Rebecca70'),Personnage( 2,'Emir', 18, 'humain',200,'épéiste','Rebecca70'),Personnage(3,'Elliot', 500, 'démon',200,'épéiste','Rebecca70')])
        result[2].sort(key=lambda result[2]:result[2].id_perso)
        test[2].sort(key=lambda test[2]:test[2].id_perso)
        #THEN 
        self.assertEqual(result.pseudo,test.pseudo)
        self.assertEqual(result.age,test.age)
        self.assertEqual(len(result[2]),len(test[2]))
        

    def test_bannir_joueur(self):
        #on donne un pseudo valide
        pse= 'Hilaire100'
        #WHEN 
        test=DAO().bannir_joueur(pse)
        result=['Hilaire100','f7dc98d348d95012795b68b120e39ee078d22cbbfd7b64acd93395a75cae2459']
        #THEN 
        self.assertEqual(result[1],test[1])
        self.assertEqual(result[2],test[2])

    
    def test_verifier_mdp_true(self):
        #on donne le mot de passe a tester qui est correct pour un pseudo
        pseu=Armandblabla34!
        mdp=Rebecca70 
        #WHEN 
        test=DAO().verifier_mdp(pseu,mdp)
        #THEN
        self.assertTrue(test)
        pass

    def test_verifier_mdp_false(self):
        #on donne le mot de passe a tester qui n'est pas correct pour un pseudo
        mdp=Armandblabla34g!
        pseu=Rebecca70 
        #WHEN 
        test=DAO().verifier_mdp(pseu,mdp)
        #THEN
        self.assertFalse(test)
        pass

    def test_verifier_pseudo_libre_true(self):
        #On donne un pseudo non existant
        pseu="Boris"
        #WHEN
        test=DAO().verifier_pseudo_libre(pseu)
        #THEN 
        self.assertTrue(test)
        pass

    def test_verifier_pseudo_libre_false(self):
        #On donne un pseudo  existant
        pseu='Rebecca70'
        #WHEN
        test=DAO().verifier_pseudo_libre(pseu)
        #THEN 
        self.assertFalse(test)







