from unittest import TestCase

from dao.dao import DAO

from objets_metiers.joueur import Joueur
from objets_metiers.personnage import Personnage

class TestDaoJoueur(TestCase):

    def test_liste_joueur(self):
        #liste des joueurs pre renseignés
        result=[Joueur('Rebecca70', 24,[Personnage(1,'Elyanna', 200,'elf',200, 'enchantresse','Rebecca70'),Personnage(2, 'Emir', 18, 'humain',200,'épéiste','Rebecca70'),Personnage(3,'Elliot', 500, 'démon',200,'épéiste','Rebecca70')]),
        Joueur('Aimee20', 36, [Personnage(4'Blondinet', 200, 'nain',50, 'enchanteur','Aimee20'), Personnage(5,'Erys', 30, 'humain',100,'roi','Aimee20'),Personnage(6, 'Lucifer', 800, 'démon',300'enchanteur','Aimee20')]),
        Joueur( 'Marielle90', 27,[Personnage( (7,'Elodie', 200, 'elf',20 'enchantresse','Marielle90'),Personnage( 8,'Aymen', 180, 'dragon','combattant',200,'Marielle90'), Personnage(9, 'Amor', 20, 'humain',200,'enchantresse','Marielle90')]),
        Joueur('Hilaire100', 58,[Personnage (10,'Isabella', 200,'elf',20,'enchantresse','Hilaire100'),Personnage( 11,'Arthur', 18, 'humain',200,'prince','Hilaire100'),Personnage(12, 'Orifice', 500,  'démon',200, 'forgeron', 'Hilaire100')])]
        # WHEN
        test=DAO().liste_joueurs()
        result[].sort(key=lambda result[]:result[].age)
        test[].sort(key=lambda test[]:test[].age)
        result[][2].sort(key=lambda result[][2]:result[][2].id_perso)
        test[][2].sort(key=lambda test[][2]:test[][2].id_perso)
        #THEN
        self.assertEqual(result,test)
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

    def test_creer_perso(self):
        # GIVEN
        perso = Personnage(id=None, nom="Fafnir", age=135, race="Dwarf", niveau=50, classe="Ranger", pseudo_j="Westbric00")
        # WHEN
        res=DAO().creer_perso(perso)
        #THEN
        self.assertIsInstance(res, int)

    def test_chercher_par_pseudo_j(self):
        # On donne un psuedo valide
        pseudo_val="Rebecca70"
        # WHEN
        test=DAO().chercher_par_pseudo_j(pseudo_val)
        result=Joueur("Rebecca70",24, [Personnage(1,'Elyanna', 200,'elf',200, 'enchantresse','Rebecca70'),Personnage( 2,'Emir', 18, 'humain',200,'épéiste','Rebecca70'),Personnage(3,'Elliot', 500, 'démon',200,'épéiste','Rebecca70')])
        result[2].sort(key=lambda result[2]:result[2].id_perso)
        test[2].sort(key=lambda test[2]:test[2].id_perso)
        #THEN 
        self.assertEqual(result,test)
        pass

    def test_bannir_joueur(self):
        #on donne un pseudo valide
        pse= 'Hilaire100'
        #WHEN 
        test=DAO().bannir_joueur(pse)
        result='Hilaire100','f7dc98d348d95012795b68b120e39ee078d22cbbfd7b64acd93395a75cae2459'
        #THEN 
        self.assertEqual(result,test)
        pass

    
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

    def test_chercher_msg_par_pseudo(self):
        #on donne un pseudo 
        pseu=Rebecca70 
        







