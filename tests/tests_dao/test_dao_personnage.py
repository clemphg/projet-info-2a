from itertools import combinations_with_replacement
from unittest import TestCase

from dao.dao import DAO

from objets_metiers.personnage import Personnage

class TestDaoPersonnage(TestCase):

    def test_liste_personnages(self):
        #on a la liste de tous les personnages
        result=[Personnage(1,'Elyanna', 200,'elf',200, 'enchantresse','Rebecca70'),Personnage(2, 'Emir', 18, 'humain',200,'épéiste','Rebecca70'),Personnage( 3,'Elliot', 500, 'démon', 200,'épéiste','Rebecca70'),Personnage(4,'Blondinet', 200, 'nain', 50, 'enchanteur','Aimee20'),Personnage(5,'Erys', 30,  'humain',100,'roi','Aimee20'),
        Personnage(6, 'Lucifer', 800, 'démon', 300,'enchanteur','Aimee20'),Personnage(7,'Elodie', 200,'elf',  20,'enchantresse','Marielle90'),Personnage(8, 'Aymen', 180,  'dragon',200,'combattant','Marielle90'),
        Personnage(9, 'Amor', 20, 'humain', 200,'enchantresse','Marielle90'),Personnage(10,'Isabella', 200,'elf', 20,'enchantresse','Hilaire100'),Personnage(11, 'Arthur', 18,  'humain',200,'prince','Hilaire100'),Personnage(12, 'Orifice', 500, 'démon', 200, 'forgeron', 'Hilaire100')]
        #WHEN
        test=DAO().liste_personnages()
        result[2].sort(key=lambda result[2]:result[2].id_perso)
        test[2].sort(key=lambda test[2]:test[2].id_perso)
        #THEN
        self.assertEqual(result,test)
        pass
    
    
    
    def test_creer_personnage(self):
        # On donne un  Personage
        perso=Personnage("Knight20",20,"demi_orc",102,"barbare","Aimee20")
        # WHEN
        tets=DAO().creer_perso(perso)
        #THEN
        self.assertTrue(test)
        pass

    def test_chercher_par_id_perso(self):
        # On donne un id valide
        id_val=1
        # WHEN
        test=DAO().chercher_par_id_perso(id_val)
        result=Personnage(1,'Elyanna', 200,'elf',200, 'enchantresse','Rebecca70')
        #THEN 
        self.assertEqual(result,test))
        pass
    
    def test_inscription_personnage(self):
        #on donne un id_perso, id-partie valide
        inscrip=(2,1)
        # WHEN
        test=DAO().inscription_personnage(inscip)
        #THEN
        self.assertTrue(test)

    def test_maj_classe(self):
        # On donne une nouvelle classe et la classe actuelle du personange
        nouvelle_c="combattant"
        perso= Personnage(9, 'Amor', 20, 'humain', 200,'enchantresse','Marielle90')
        # WHEN
        test=DAO().maj_classe(perso,nouvelle_c)
        #THEN 
        self.assertTrue(test)
        pass
    
    

        
        


    