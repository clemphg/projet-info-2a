from abc import ABC, abstractmethod

class AbstractJoueur(ABC):

    def __init__(self, pseudo, age):
        self.__pseudo = pseudo
        self.__age = age

    @abstractmethod
    def desistement():
        pass