from unittest import TestCase

from objets_metiers.partie import Partie
from objets_metiers.scenario import Scenario
from objets_metiers.personnage import Personnage



class TestPartie(TestCase):

    def test_id(self):
        # GIVEN
        identifiant = 19
        # WHEN
        partie = Partie(id=identifiant)
        # THEN
        self.assertEqual(identifiant,partie.id)

    def test_id_setter(self):
        # GIVEN
        partie = Partie(id=19)
        nv_id = 14
        # WHEN
        partie.id = nv_id
        # THEN
        self.assertEqual(nv_id,partie.id)

    def test_creneau(self):
        # GIVEN
        cren = 1
        # WHEN
        partie = Partie(creneau=cren)
        # THEN
        self.assertEqual(cren,partie.creneau)

    def test_scenario(self):
        # GIVEN
        scenar = Scenario(nom="A l'aventure")
        # WHEN
        partie = Partie(scenario=scenar)
        # THEN
        self.assertEqual(scenar,partie.scenario)

    def test_str(self):
        # GIVEN
        scenar = Scenario(nom="A l'aventure")
        # WHEN
        res = scenar.__str__()
        # THEN
        self.assertIsInstance(res,str)