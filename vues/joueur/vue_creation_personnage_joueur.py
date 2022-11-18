from pprint import pprint
import regex

from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

from objets_metiers.personnage import Personnage

# importation des vues
from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_joueur import ServiceJoueur
# importation des services
from client.client_personnage import ClientPersonnage
class ValidationInput(Validator):

    def validate(self, document):
        ''' Permet de vérifier que le texte rentré ici défini comme document ait bien un nombre de caractères compris entre
        5 et 25 avec une majuscule uniquement pour la première lettre, et affiche un message d'erreur si ce n'est pas le cas  '''

        ok = regex.match("^[A-Z]{0,1}[a-z]{5,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un nom valide (entre 5 et 25 caractères, majuscule uniquement pour la première lettre)',
                cursor_position=len(document.text)
            )

class ValidationEntier(Validator):

    def validate(self, document):
        ''' Permet de vérifier que le nombre rentré ici défini comme document soit bien un entier, et affiche un message d'erreur si ce n'est pas le cas  '''

        ok = regex.match("^\d{1,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un entier',
                cursor_position=len(document.text)
            )



class VueCreationPersonnageJoueur(AbstractVue):
    def __init__(self) -> None:
        ''' Création de la vue avec la définition d'une variable questions qui va stocker les intéractions du joueur,
        qui consitent à pouvoir choisir le nom de son personnage, son âge, son niveau et sa classe s'il sélectionne
        'Créer le personnage'. Il pourra également abandonner la création de son personnage en sélectionnant 'Abandonner'
        et/ou retourner sur le menu principal en sélectionnant 'Retourner au menu principal'
        '''
        self.__questions = [
            {
                'type': 'input',
                'name': 'choix_nom',
                'message': 'Nom',
                'validate': ValidationInput
            },
            {
                'type': 'input',
                'name': 'choix_age',
                'message': 'Age',
                'validate': ValidationEntier
            },
            {
                'type': 'list',
                'name': 'choix_race',
                'message': 'Race',
                'choices': ClientPersonnage().races_possibles()
            },
            {
                'type': 'input',
                'name': 'choix_niveau',
                'message': 'Niveau',
                'validate': ValidationEntier
            },
            {
                'type': 'list',
                'name': 'choix_classe',
                'message': 'Classe',
                'choices': ClientPersonnage().classes_possibles()
            },
            {
                'type': 'list',
                'name': 'validation',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Créer le personnage',
                    'Abandonner'
                ]
            },
            {
                'type': 'list',
                'name': 'menu_suivant',
                'message': '',
                'choices': [
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        ''' Permet d'afficher sur la console 'Création d'un personnage' '''
        print("Création d'un personnage")

    def make_choice(self):
        ''' Permet d'afficher le menu à partir de la variable question. Ce qui s'affichera dépendra du choix sélectionné par le joueur.
        Si le joueur décide de sélectionner 'Créer le personnage' sur le menu, il pourra créer le personnage de son choix à condition que
        le nombre de personnages qu'il possède déjà ne dépasse pas 3, ainsi un message s'affichera comme quoi le création a bien eu lieu.
        De plus, le personnage nouvellement créé sera stocké dans la base de données. Dans le cas contraire, un message d'erreur s'affichera.
        Le joueur pourra ensuite choisir de retourner au menu principal. Si c'est le cas, la vue principale du joueur sera retournée  '''

        # si le joueur peut encore créer un personnage
        if len(Session().utilisateur.personnages)<3:
            reponses = prompt(self.__questions[0:6])

            if reponses['validation'] == 'Créer le personnage':
                perso = Personnage(nom=reponses['choix_nom'],
                                   age=reponses['choix_age'],
                                   race=reponses['choix_race'],
                                   niveau=int(reponses['choix_niveau']),
                                   classe=reponses['choix_classe'],
                                   pseudo_j=Session().utilisateur.pseudo)
                id = ServiceJoueur().creation_personnage(perso)
                Session().utilisateur.creer_personnage(id=id,
                                                       nom=reponses['choix_nom'],
                                                       age=reponses['choix_age'],
                                                       race=reponses['choix_race'],
                                                       niveau=int(reponses['choix_niveau']),
                                                       classe=reponses['choix_classe'])
                print('Le personnage a bien été créé !')
        else:
            print("Vous avez déjà trois personnages, vous ne pouvez pas en créer plus.\n"
                  "Vous pouvez modifier la classe de vos personnages dans le menus 'Mes personnages'.\n")

        # retour au menu principal
        suivant = prompt(self.__questions[6])
        if suivant['menu_suivant'] == 'Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()
        else :
            pass
