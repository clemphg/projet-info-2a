from unittest import TestCase
from objets_metiers.organisateur import Organisateur

from objets_metiers.partie import Partie
from objets_metiers.scenario import Scenario
from objets_metiers.personnage import Personnage



class TestOrganisateur(TestCase):

    def test_pseudo(self):
        # GIVEN
        pseudo = "loulou"
        # WHEN
        org = Organisateur(pseudo=pseudo)
        # THEN
        self.assertEqual(pseudo,org.pseudo)