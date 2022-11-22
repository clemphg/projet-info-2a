from unittest import TestCase
from objets_metiers.organisateur import Organisateur


class TestOrganisateur(TestCase):

    def test_pseudo(self):
        # GIVEN
        pseudo = "loulou"
        # WHEN
        org = Organisateur(pseudo=pseudo)
        # THEN
        self.assertEqual(pseudo,org.pseudo)