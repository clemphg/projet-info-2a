

class Partie():

    def __init__(self, date, scenario, table):
        self.__date = date
        self.__scenario = scenario
        self.__liste_persos = None
        self.__table = table

    def ajouter_perso(self, perso):
        if self.__liste_persos and len(self.__liste_persos)<5 :
            self.__liste_persos.append(perso)
        elif len(self.__liste_persos)<5:
            self.__liste_persos = [perso]

    def supprimer_perso(self, perso):
        pass