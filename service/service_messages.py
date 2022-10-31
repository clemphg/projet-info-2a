from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO


class ServiceMessages(metaclass=Singleton):

    def chercher_messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)