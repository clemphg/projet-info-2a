from objets_metiers.abstract_joueur import AbstractJoueur
from objets_metiers.personnage import Personnage

class Joueur(AbstractJoueur):

    def __init__(self, pseudo, age, personnages = []):
        super().__init__(pseudo, age)
        self.__personnages = personnages

    @property
    def personnages(self):
        return self.__personnages

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
        if len(self.__personnages)<2:
            self.__personnages.append(Personnage(nom, age, race, niveau, classe))
            status = True
        else:
            status = False
        return status

    def inscription_partie():
        pass