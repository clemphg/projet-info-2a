from utils.singleton import Singleton


class DAO(Singleton):
    CONNECTION=.....
    def creer_joueur(joueur: Joueur):
        with connection.cursor() as cursor :
            curseur.execute("INSERT INTO joueur (pseudo_j , mot_de_passe, age)"
            "VALUES (%(pseudo)s, %(mdp)s,%(age)s) RETURNING id_joueur;" 
            ,{
                "pseudo" : joueur.pseudo,
                "name" : joueur.mot_de_passe
                "description" : joueur.description
                })
            joueur.id = curseur.fetchone()[0]
        return joueur.id


