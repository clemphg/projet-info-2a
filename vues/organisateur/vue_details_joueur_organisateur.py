from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

from service.service_organisateur import ServiceOrganisateur


class VueDetailsJoueurOrganisateur(AbstractVue):
    def __init__(self, joueur) -> None:
        self.__joueur = joueur
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Bannir ce joueur',
                    "Supprimer l'un de ses personnages",
                    'Retour à la liste des joueurs',
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'retour',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix_perso',
                'message': 'Sélectionner un personnage (selon son id)',
                'choices': [
                    str(perso.id) for perso in self.__joueur.personnages
                ]
            }
        ]

    def display_info(self):
        print("-- Détails sur un joueur --\n")

        print(self.__joueur,"\n")

    def make_choice(self):
        reponse = prompt(self.__questions[0])

        if reponse['choix'] == "Bannir ce joueur":
            res = ServiceOrganisateur().bannir_joueur(self.__joueur)
            if res:
                print("Le joueur ", self.__joueur.pseudo," a bien été banni.")
            reponse = prompt(self.__questions[1])
            if reponse['retour']=='Retourner au menu principal':
                from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                return VuePrincipaleOrganisateur()
        elif reponse['choix'] == "Supprimer l'un de ses personnages":
            if len(self.__joueur.personnages)==0:
                print("Ce joueur n'a aucun personnage.")
                reponse = prompt(self.__questions[1])
                if reponse['retour']=='Retourner au menu principal':
                    from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                    return VuePrincipaleOrganisateur()
            else:
                reponse = prompt(self.__questions[2])
                id_perso = reponse['choix_perso']
                perso = [perso for perso in self.__joueur.personnages if perso.id==int(id_perso)][0]
                res = ServiceOrganisateur().supprimer_personnage(perso, self.__joueur)
                if res:
                    print("Le personnage a bien été supprimé.")
                reponse = prompt(self.__questions[1])
                if reponse['retour']=='Retourner au menu principal':
                    from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                    return VuePrincipaleOrganisateur()

        elif reponse['choix'] == 'Retour à la liste des joueurs':
            from vues.organisateur.vue_joueurs_organisateur import VueJoueursOrganisateur
            return VueJoueursOrganisateur()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()
        else:
            pass