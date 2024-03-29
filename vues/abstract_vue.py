from abc import ABC, abstractmethod

from vues.session import Session


class AbstractVue(ABC):

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def make_choice(self):
        pass
