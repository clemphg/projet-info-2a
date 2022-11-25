from unittest import TestCase

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario
<<<<<<< HEAD

class TestDaoMaitredejeu(TestCase):

    
    def test_liste_mjs(self):  
        # WHEN
        test=DAO().liste_mjs()
        #THEN
        self.assertEqual(len(test),4)
        self.assertIsInstance(test[1],MaitreDeJeu)
        pass
    
    
    def test_creer_mj(self):
        # On donne un couple mj, mdp valide
        Mj=[MaitreDeJeu("Brich52",34),Brandito62*]
        # WHEN
        tets=DAO().creer_mj(Mj[0],Mj[1])
        #THEN
        self.assertTrue(test)
        pass

    def test_chercher_par_pseudo_mj(self):
        # On donne un psuedo valide
        pseudo_val="GiGigigi"
        # WHEN
        test=DAO().chercher_par_pseudo_mj(pseudo_val)
        result=MaitreDeJeu("GiGigigi",25,[Scenario(1,'Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGigigi'),Scenario(2,'Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGigigi')])
        #THEN 
        self.assertEqual(result,test))
        self.assertEqual(result.pseudo,test.pseudo)
        self.assertEqual(result.age,test.age)
        self.assertEqual(len(result[2]),len(test[2]))

    def test_bannir_joueur(self):
        #on donne un pseudo valide
        pse= 'Hihi100'
        #WHEN 
        test=DAO().bannir_mj(pse)
        result=['Hihi100','f45ee875ec85143d36410b2bae622e6bbcef9e344e7528d219cb112a0116cc63']
        #THEN 
        self.assertEqual(result[1],test[1])
        self.assertEqual(result[2],test[2])
        



