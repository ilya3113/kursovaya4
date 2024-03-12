import json

from scr.config import DATA
from scr.AbstractJSON import AbstractJSON
from scr.GetVacancies import GetVacancies
class JsonFail(AbstractJSON,GetVacancies):
    def __init__(self, name_vacancy: str):
        super().__init__(name_vacancy)
        self.message = "Найденные вакансии"

    def __repr__(self):
        return f"{self.all_vacancy}"
    def save_info(self) -> str or list:
        """
        Создан json-файл с информацией о вакансиях
        """

        if len(self.all_vacancy) == 0:
            self.message = "Вакансия не найдена"
            return self.message
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
            return self.all_vacancy
