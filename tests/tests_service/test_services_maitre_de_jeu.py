from unittest import TestCase

from service.service_maitre_de_jeu import ServiceMaitreDeJeu

from objets_metiers.partie import Partie

from objets_metiers.scenario import Scenario
from objets_metiers.maitre_de_jeu import MaitreDeJeu


class TestServiceMaitreDeJeu(TestCase):

    def test_creer_scenario(self):
        # GIVEN
        scenario=Scenario(id=None, nom="aventure", description="une grande aventure", niveau_min=100, pseudo_mj="Amy10")
        # WHEN
        res=ServiceMaitreDeJeu().creer_scenario(scenario)
        #THEN
        self.assertIsInstance(res,int)

    def test_creer_partie(self):
        # GIVEN
        scenario=Scenario(id=None, nom="aventure", description="une grande aventure", niveau_min=100, pseudo_mj="Amy10")
        partie = Partie(id=None, creneau = 1, scenario=scenario)
        # WHEN
        res=ServiceMaitreDeJeu().creer_partie(partie)
        #THEN
        self.assertIsInstance(res,int)

    def test_details_partie(self):
        # GIVEN
        id_partie = 1
        # WHEN
        res=ServiceMaitreDeJeu().details_partie(id_partie)
        #THEN
        self.assertIsInstance(res,Partie)

    def test_liste_parties(self):
        # GIVEN
        pseudo_mj = "Amy10"
        # WHEN
        res=ServiceMaitreDeJeu().liste_parties(pseudo_mj)
        #THEN
        self.assertIsInstance(res,list)

    def test_liste_creneaux_dispo(self):
        # GIVEN
        mj = MaitreDeJeu(pseudo = "Marie18", age=28)
        # WHEN
        res=ServiceMaitreDeJeu().liste_creneaux_dispos(mj)
        #THEN
        self.assertIsInstance(res,list)

    def test_supprimer_partie_possible(self):
        # GIVEN
        partie = ServiceMaitreDeJeu().details_partie(3)
        # WHEN
        res=ServiceMaitreDeJeu().supprimer_partie(partie)
        #THEN
        self.assertTrue(res)