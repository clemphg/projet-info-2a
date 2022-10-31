from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

from objets_metiers.joueur import Joueur

class ServiceJoueur(metaclass=Singleton):

    def messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)
