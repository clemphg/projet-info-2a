from unittest import TestCase

from service.service_organisateur import ServiceOrganisateur


class TestServiceOrganisateur(TestCase):

    def test_liste_joueurs(self):
        # GIVEN

        # WHEN
        res=ServiceOrganisateur().liste_joueurs()
        #THEN
        self.assertIsInstance(res,list)

    def test_liste_mjs(self):
        # GIVEN

        # WHEN
        res=ServiceOrganisateur().liste_mjs()
        #THEN
        self.assertIsInstance(res,list)
