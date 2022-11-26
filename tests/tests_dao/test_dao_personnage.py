from itertools import combinations_with_replacement
from unittest import TestCase

from dao.dao import DAO

from objets_metiers.personnage import Personnage

class TestDaoPersonnage(TestCase):

    def test_liste_personnages(self):
        test=DAO().liste_personnages()
        #THEN
        self.assertIsInstance(test[1],Personnage)
        
    
    
    def test_creer_personnage(self):
        # On donne un  Personage
        perso=Personnage(id=None,"Knight20",20,"demi_orc",102,"barbare","Aimee20")
        # WHEN
        tets=DAO().creer_perso(perso)
        #THEN
        self.assertTrue(test)
        

    def test_chercher_par_id_perso(self):
        # On donne un id valide
        id_val=1
        # WHEN
        test=DAO().chercher_par_id_perso(id_val)
        result=Personnage(1,'Elyanna', 200,'elf',200, 'enchantresse','Rebecca70')
        #THEN 
        self.assertEqual(result[1],test[1])
    
    
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
       
    def test_supprimer_perso(self):
        #On donne un perso a supprimer
        perso=Personnage(4,'Blondinet', 200, 'nain', 50, 'enchanteur','Aimee20')
        #WHEN 
        test=DAO().supprimer_personnage(perso)
        #THEN 
        self.assertTrue(test)

    


    

        
        


    