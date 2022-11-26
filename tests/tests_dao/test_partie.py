from itertools import combinations_with_replacement
from unittest import TestCase
from objets_metiers.partie import Partie
from dao.dao import DAO

from objets_metiers.scenario import Scenario
from objets_metiers.personnage import Personnage

class TestDaoPartie(TestCase):

    def test_ajouter_joueur_partie(self):
        #GIVEN
        partie=Partie(3,
                      5,
                      Scenario(5,'Bataille navale', 'Le jeu se déroulera sous l eau',100,'Marie18'),
                      [Personnage(2,'Emir', 18, 'humain', 200,'épéiste','Rebecca70'),
                       Personnage(4,'Blondinet', 200, 'nain', 50, 'enchanteur','Aimee20'),
                       Personnage(7,'Elodie', 200, 'elf',20, 'enchantresse','Marielle90'),
                       Personnage(11, 'Arthur', 18, 'humain', 200,'prince','Hilaire100')])
        perso=Personnage(12, 'Orifice', 500, 'démon', 200, 'forgeron', 'Hilaire100')
        #WHEN
        test=DAO().ajouter_joueur_partie(partie,perso)
        #THEN
        self.assertTrue(test)


    def test_supprimer_partie(self):
        #On donne une partie existante
        p=Partie(4,
                 6,
                 Scenario(6,'Bataille dans le ciel', 'Le jeu se déroulera dans le ciel mais attention aux licornes armées',50,'Marie18'),
                 [Personnage(1,'Elyanna', 200, 'elf',200, 'enchantresse','Rebecca70'),
                  Personnage(5,'Elyanna', 200,'elf',  200,'enchantresse','Rebecca70'),
                  Personnage(8, 'Aymen', 180, 'dragon', 200,'combattant','Marielle90'),
                  Personnage(12, 'Orifice', 500, 'démon', 200, 'forgeron', 'Hilaire100')])
        #WHEN
        res=DAO().supprimer_partie(p)
        #THEN
        self.assertTrue(res)
