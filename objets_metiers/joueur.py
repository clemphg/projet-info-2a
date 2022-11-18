from objets_metiers.abstract_joueur import AbstractJoueur
from objets_metiers.personnage import Personnage


class Joueur(AbstractJoueur):
    ''' Un joueur est un abstract joueur défini par son pseudo, son âge et la liste de personnages qu'il possède
        Attributes
        ----------
        pseudo : str
            Le pseudo du joueur
        age : int
            L'âge du joueur
        personnages : liste
            Liste de personnages que possède le joueur, il peut en avoir maximum 3, au départ elle est vide

        Examples
        ----------
        Exemple d'utilisation
        >>> c = Joueur()
        >>> c.creer_personnage()
        '''
    def __init__(self, pseudo, age, personnages = []):
        ''' Constructeur'''
        super().__init__(pseudo, age)
        self.__personnages = personnages

    @property
    def personnages(self):
        return self.__personnages

    def __str__(self):
        res = "Pseudo     : {pseudo}\nAge        : {age}".format(pseudo=self.pseudo, age=self.age)
        if len(self.__personnages)>0:
            res = res+"\nPersonnage :"
            for perso in self.__personnages:
                res = res+"\n"+perso.__str__()
        return res

    def creer_personnage(self, nom, age, race, niveau, classe):
        """Création d'un personnage.

        Un joueur possède des personnages. Il peut en créer jusqu'à trois. Il s'inscrit sur
        une partie en précisant le personnage avec lequel il veut jouer.

        Parameters
        ----------
        nom : str
            Nom du personnage.
        age : int
            Age du personnage.
        race : str
            Race du personnage (la liste des races possibles est déterminée à partir de https://www.dnd5eapi.co/ )
        niveau : int
            Niveau du personnage
        classe : str
            Classe du personnage (la liste des races possibles est déterminée à partir de https://www.dnd5eapi.co/ )

        Returns
        -------
        bool
            True si le personnage a bien été ajouté, False sinon
        """
        from dao.dao import DAO
        if len(self.__personnages)<3:
            perso = Personnage(nom=nom,
                               age=age,
                               race=race,
                               niveau=niveau,
                               classe=classe,
                               pseudo_j=self.pseudo)
            id = DAO().creer_perso(perso)
            perso.id = id
            self.__personnages.append(perso)
            status = True
            from service.service_messages import ServiceMessages
            ServiceMessages().message_creation_personnage(self.pseudo, perso)
        else:
            status = False
        return status
