from abc import ABC, abstractmethod


class AbstractHh(ABC):

    @abstractmethod
    def get_vacancy_from_api(self):
        pass
