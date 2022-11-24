from utils.singleton import Singleton

from datetime import datetime

from dao.dao import DAO


class ServiceMessages(metaclass=Singleton):

    def chercher_messages(self, pseudo):
        "Renvoie la liste des messages de l'utilisateur à l'aide de son pseudo"
        return DAO().chercher_messages_par_pseudo(pseudo)

    def message_inscription(self, pseudo):
        "Vérifie si on a bien envoyé le message d'inscription suivant:'Inscription sur la plateforme', daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Inscription sur la plateforme."
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_creation_personnage(self, pseudo, perso):
        "Vérifie si on a bien envoyé le message de création d'un personnage, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Création du personnage {id} ({nom}, {age} ans, niveau {niv}, {race}, {classe}).".format(id = perso.id, nom = perso.nom, age = perso.age,
                                                                                                      niv = perso.niveau, race = perso.race, classe = perso.classe)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_maj_classe(self, pseudo, perso, nvlle_classe):
        "Vérifie si on a bien envoyé le message de changement de classe du personnage voulu, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Le personnage {id} ({nom}, {age} ans, niveau {niv}, {race}) passe de {classe} à {nv_classe}.".format(id = perso.id, nom = perso.nom,
                                                                                                                    age = perso.age, niv = perso.niveau,
                                                                                                                    race = perso.race, classe = perso.classe,
                                                                                                                    nv_classe = nvlle_classe)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_creation_scenario(self, pseudo, scenario):
        "Vérifie si on a bien envoyé le message de création du scénario, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Création du scénario {id} ({nom}, niveau minimum : {niv_min}).".format(id = scenario.id, nom = scenario.nom, niv_min = scenario.niveau_min)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_creation_partie(self, pseudo, partie):
        "Vérifie si on a bien envoyé le message de création d'une partie, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Création de la partie {id} (scénario : {nom}, niveau minimum : {niv_min}, creneau {cr}).".format(id = partie.id, nom = partie.scenario.nom,
                                                                                                                niv_min = partie.scenario.niveau_min,
                                                                                                                cr = partie.creneau)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_suppression_partie(self, pseudo, partie):
        "Vérifie si on a bien envoyé le message de suppression de stage, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Suppression de la partie {id} (scénario : {nom}, niveau minimum : {niv_min}, creneau {cr}).".format(id = partie.id, nom = partie.scenario.nom,
                                                                                                                   niv_min = partie.scenario.niveau_min,
                                                                                                                   cr = partie.creneau)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_inscription_partie(self, pseudo, id_partie, id_perso):
        "Vérifie si on a bien envoyé le message d'inscription à une partie, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Inscription à la partie {id_partie} avec le personnage {id_perso}.".format(id_partie=id_partie, id_perso=id_perso)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_desinscription_partie(self, pseudo, id_partie, id_perso):
        "Vérifie si on a bien envoyé le message de désinscription à une partie, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Désinscription du personnage {id_perso} de la partie {id_partie}.".format(id_perso=id_perso, id_partie=id_partie)
        status = DAO().ajouter_message(pseudo, date, msg)
        return status

    def message_suppression_perso_org(self, pseudo_j, pseudo_o, perso):
        "Vérifie si on a bien envoyé le message de suppression du personnage par l'organisateur, daté à l'utilisateur. Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Votre personnage {id_perso} ({nom}, {age} ans, niveau {niv}, {race}, {classe}) a été supprimé par {pseudo_o}.".format(id_perso=perso.id,
                                                                                                                                     nom = perso.nom,
                                                                                                                                     age = perso.age,
                                                                                                                                     niv = perso.niveau,
                                                                                                                                     race = perso.race,
                                                                                                                                     classe = perso.classe,
                                                                                                                                     pseudo_o=pseudo_o)
        status = DAO().ajouter_message(pseudo_j, date, msg)
        return status

    def message_suppression_scenario_org(self, pseudo_mj, pseudo_o, scenario):
        "Vérifie si on a bien envoyé le message de suppression du scénario par l'organisateur, daté à l'utilisateur (généralement le maître de jeu). Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Suppression du scénario {id} ({nom}, niveau minimum : {niv_min}) par {pseudo_o}.".format(id = scenario.id, nom = scenario.nom,
                                                                                                        niv_min = scenario.niveau_min, pseudo_o=pseudo_o)
        status = DAO().ajouter_message(pseudo_mj, date, msg)
        return status

    def message_desinscription_partie_org(self, pseudo_j, pseudo_o, id_partie, id_perso):
        "Vérifie si on a bien envoyé le message de suppression de désinscription par l'organisateur, à l'utilisateur (généralement le joueur). Si c'est le cas, la méthode retourne True sinon False"
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg = "Vous avez été désinscrit de la partie {id_partie} (personnage {id_perso} par {pseudo_o}.".format(id_partie=id_partie, id_perso=id_perso, pseudo_o=pseudo_o)
        status = DAO().ajouter_message(pseudo_j, date, msg)
        return status
