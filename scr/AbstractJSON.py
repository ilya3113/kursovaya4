from abc import ABC, abstractmethod


class AbstractJSON(ABC):
    @abstractmethod
    def save_info(self):
        pass