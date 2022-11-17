from email import message
from utils.singleton import Singleton

from datetime import datetime

from vues.session import Session

from dao.dao import DAO


class ServiceMessages(metaclass=Singleton):

    def chercher_messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)

    def message_inscription(self, pseudo):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Inscription"
        DAO().ajouter_message(pseudo, date, msg)

