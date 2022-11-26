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
        perso=Personnage(id=None,nom="Knight20",age=20,race="Hal-Orc",niveau=102,classe="Barbarian",pseudo_j="Aimee20")
        # WHEN
        res=DAO().creer_perso(perso)
        #THEN
        self.assertIsInstance(res, int)


    def test_chercher_par_id_perso(self):
        #GIVEN
        perso=Personnage(1,'Elyanna', 200,'Elf',200, 'Wizard','Rebecca70')
        # WHEN
        res=DAO().chercher_par_id_perso(perso.id)
        #THEN
        self.assertEqual(perso.id,res.id)
        self.assertEqual(perso.nom,res.nom)
        self.assertEqual(perso.age,res.age)
        self.assertEqual(perso.race,res.race)
        self.assertEqual(perso.niveau,res.niveau)
        self.assertEqual(perso.race,res.race)


    def test_inscription_personnage(self):
        #GIVEN
        id_partie = 4
        id_perso = 12
        # WHEN
        test=DAO().inscription_personnage(id_perso, id_partie)
        #THEN
        self.assertTrue(test)

    def test_maj_classe(self):
        # GIVEN
        nouvelle_c="Fighter"
        perso= Personnage(9, 'Amor', 20, 'Human', 200,'Rogue','Marielle90')
        # WHEN
        test=DAO().maj_classe(perso,nouvelle_c)
        #THEN
        self.assertTrue(test)










