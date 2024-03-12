import json
from typing import Any

import requests

from scr.config import DATA
from scr.AbstractHh import AbstractHh

class GetVacancies(AbstractHh):
    all = []

    def __init__(self, name_vacancy: str):
        self.name_vacancy: str = name_vacancy
        self.message = "Найденные вакансии"
        self.all_vacancy = self.get_vacancy_from_api()

    def get_vacancy_from_api(self) -> str | Any:
        """
        Получите достоверную информацию о вакансиях для пользователя
        """

        if isinstance(self.name_vacancy, str):
            keys_response = {'text': f'NAME:{self.name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']
        else:
            self.message = "Вакансия не найдена"
            return self.message
