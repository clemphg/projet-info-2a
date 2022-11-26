from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

from service.service_organisateur import ServiceOrganisateur

class VueInscriptionPartieOrganisateur(AbstractVue):
    def __init__(self, partie) -> None:
        self.__partie = partie
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Validation',
                'choices': [
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Validation',
                'choices': [
                    "Confirmer l'inscription",
                    "Annuler"
                ]
            }
        ]

    def display_info(self):
        print(" --- Inscrire un personnage à la partie --- \n")
        print(self.__partie,"\n")

    def make_choice(self):
        # personnages de joueurs disponibles et de niveau suffisant
        persos_possibles = ServiceOrganisateur().personnages_possibles(self.__partie)
        if len(persos_possibles)>0:
            reponse = prompt(
                {
                    'type': 'list',
                    'name': 'choix',
                    'message': 'Validation',
                    'choices':
                        ["ID : "+str(p.id)+" , Nom : "+p.nom+" , Race : "+p.race+" , Classe : "+p.classe+" , Niveau : "+str(p.niveau) for p in persos_possibles]
                }
            )
            id_perso = int(reponse['choix'].split(' ')[2])
            perso = [p for p in persos_possibles if p.id==id_perso][0]
            reponse = prompt(self.__questions[1])
            if reponse['choix']=="Confirmer l'inscription":
                res = ServiceOrganisateur().inscrire_personnage(perso, self.__partie)
                if res:
                    print("Le personnage a bien été inscrit.\n")
            else:
                pass

        else:
            print("Aucun personnage ne correspond aux critères pour être inscrits à cette partie.\n")

        reponse = prompt(self.__questions[0])
        if reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()
        else:
            pass