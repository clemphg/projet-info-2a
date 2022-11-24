from unittest import TestCase

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.scenario import Scenario

class TestDaoMaitredejeu(TestCase):

    
    def test_liste_mjs(self):
        #liste des mjs pre renseignés
        result=[MaitreDeJeu('GiGigigi', 25,[Scenario(1,'Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGigigi'),Scenario(2,'Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGigigi')],
        MaitreDeJeu('Amy10', 22,[Scenario(3,'Mer enchantée','Le jeu se déroulera dans une mer infestée de sirènes croqueuses d hommes', 200,'Amy10'), Scenario(4,'Montagne à dents de scie', 'Le jeu se déroulera dans une montagne infestée d ours mutants', 50,'Amy10')]),
        MaitreDeJeu('Marie18', 28,[Scenario(5,'Bataille navale', 'Le jeu se déroulera sous l eau',100,'Marie18'),Scenario(6,'Bataille dans le ciel', 'Le jeu se déroulera dans le ciel mais attention aux licornes armées',50,'Marie18')])
        MaitreDeJeu ('Hil100', 60, [Scenario(7,'Sable bouillant', 'Le but est de traverser le désert mais le sable est bouillant', 20, 'Hil100'),Scenario(8,'Sauver la princesse', 'Le but est de sauver la princesse Emily mais attention aux ogres', 80,'Hil100')])]
        # WHEN
        test=DAO().liste_mjs()
        result[].sort(key=lambda result[]:result[].age)
        test[].sort(key=lambda test[]:test[].age)
        result[][2].sort(key=lambda result[][2]:result[][2].id_scenario)
        test[][2].sort(key=lambda test[][2]:test[][2].id_scenario)
        #THEN
        self.assertEqual(result,test)
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
        result=("GiGigigi",25,[Scenario(1,'Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGigigi'),Scenario(2,'Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGigigi')])
        result[2].sort(key=lambda result[2]:result[2].id_scenario)
        test[2].sort(key=lambda test[2]:test[2].id_scenario)
        #THEN 
        self.assertEqual(result,test))
        pass

    def test_bannir_joueur(self):
        #on donne un pseudo valide
        pse= 'Hihi100'
        #WHEN 
        test=DAO().bannir_mj(pse)
        result='Hihi100','f45ee875ec85143d36410b2bae622e6bbcef9e344e7528d219cb112a0116cc63'
        #THEN 
        self.assertEqual(result,test)
        pass


    

