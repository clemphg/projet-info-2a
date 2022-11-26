"""
Création des comptes des organisateurs

Ce script permet de créer des comptes d'organisateurs avant de mettre en fonction
l'application
"""

from vues.vue_inscription_org import VueInscriptionOrg


print("Création de comptes d'organisateurs.\n")

vue_ins_org = VueInscriptionOrg()

vue_ins_org.display_info()
suivant = vue_ins_org.make_choice()

while suivant:
    suivant = vue_ins_org.make_choice()
