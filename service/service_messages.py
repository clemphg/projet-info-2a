from utils.singleton import Singleton

from datetime import datetime

from vues.session import Session

from dao.dao import DAO


class ServiceMessages(metaclass=Singleton):

    def chercher_messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)

    def message_inscription(self, pseudo):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Inscription sur la plateforme"
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_creation_personnage(self, pseudo, perso):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Création du personnage {id} ({nom}, {age} ans, niveau {niv}, {race}, {classe})".format(id = perso.id, nom = perso.nom, age = perso.age,
                                                                                                      niv = perso.niveau, race = perso.race, classe = perso.classe)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_creation_scenario(self, pseudo, scenario):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Création du scénario {id} ({nom}, niveau minimum : {niv_min})".format(id = scenario.id, nom = scenario.nom, niv_min = scenario.niveau_min)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_inscription_partie(self, pseudo, id_partie, id_perso):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Inscription à la partie {id_partie} avec le personnage {id_perso}.".format(id_partie=id_partie, id_perso=id_perso)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_desinscription_partie(self, pseudo, id_partie, id_perso):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Désinscription du personnage {id_perso} de la partie {id_partie}.".format(id_perso=id_perso, id_partie=id_partie)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status
