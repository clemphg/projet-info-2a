import imp
from pkgutil import ImpImporter
from pprint import pprint
import regex

from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator
from utils.singleton import Singleton

from vues.session import Session
from vues.abstract_vue import AbstractVue

from objets_metiers.personnage import Personnage

from dao.dao import DAO

from appel_api import AppelAPI

class ValidationInput(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Z]{0,1}[a-z]{5,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un nom valide (entre 5 et 25 caractères, majuscule uniquement pour la première lettre)',
                cursor_position=len(document.text)
            )
class ValidationEntier(Validator):
    def validate(self, document):
        ok = regex.match("^\d{1,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un entier',
                cursor_position=len(document.text)
            )



class VueCreationPersonnageJoueur(AbstractVue):
    def __init__(self) -> None:
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
                'choices': AppelAPI().races_possibles()
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
                'choices': AppelAPI().classes_possibles()
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
        print("Création d'un personnage")

    def make_choice(self):
        if len(Session().utilisateur.personnages)<3:
            reponses = prompt(self.__questions[0:6])

            if reponses['validation'] == 'Créer le personnage':
                perso = Personnage(nom=reponses['choix_nom'],
                                age=reponses['choix_age'],
                                race=reponses['choix_race'],
                                niveau=reponses['choix_niveau'],
                                classe=reponses['choix_classe'])
                id = DAO().creer_perso(perso,
                                    Session().utilisateur.pseudo)
                Session().utilisateur.creer_personnage(id=id,
                                                    nom=reponses['choix_nom'],
                                                    age=reponses['choix_age'],
                                                    race=reponses['choix_race'],
                                                    niveau=reponses['choix_niveau'],
                                                    classe=reponses['choix_classe'])
                print('Le personnage a bien été créé !')
        else:
            print("Vous avez déjà trois personnages, vous ne pouvez pas en créer plus.\n"
                  "Vous pouvez modifier la classe de vos personnages dans le menus 'Mes personnages'.\n")

        suivant = prompt(self.__questions[6])
        if suivant['menu_suivant'] == 'Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()
        else :
            pass