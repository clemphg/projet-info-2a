from abc import ABC, abstractmethod

class AbstractJoueur(ABC):

    def __init__(self, pseudo, age):
        self.__pseudo = pseudo
        self.__age = age

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def age(self):
        return self.__age

    @abstractmethod
    def desistement():
        pass