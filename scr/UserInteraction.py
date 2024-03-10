from collections import defaultdict
from scr.CompareVacancies import CompareVacancies


class UserInteraction(CompareVacancies):
    def __init__(self, name_vacancy):
        super().__init__(name_vacancy)
        self.get_vacancy_from_api()
        self.vacancies_list = defaultdict(list)

    def __str__(self):
        self.message = "Vacancy not found" if len(self.all_vacancy) == 0 else self.message
        return (f"Название вакансии для поиска: {self.name_vacancy}\n"
                f"Количество вакансии: {len(self.all_vacancy)}\n"
                f"Статус: {self.message}")

    def make_info(self, top_salary: dict) -> list:
        """
        Создан список с вакансиями для пользователя.
        param top_salary: dict с вакансиями
        пользователь хочет видеть
        :return: список с вакансиями.
        """
        print(f"Самая высокая зарплата:")

        count = 1
        for top, vacancies in top_salary.items():

            print(f"{count}. Самая высокая зарплата: {top} - количество {len(vacancies)}", end='\n')

            for value in vacancies:
                self.vacancies_list[count].extend([{"Название вакансии": value['name']},
                                                   {"Зарплата от": value['salary']['from']},
                                                   {"Зарплата до": value['salary']['to']},
                                                   {"Город": value['area']['name']},
                                                   {"URL-адрес": f"{value['alternate_url']}\n"}])
            count += 1

    @staticmethod
    def last_info(top_salary: dict, number_of_vacancies: int):
        """
        Получить информацию о топовых вакансиях
        :param number_of_vacancies: количество вакансий из топа
        :param top_salary:  список с топовыми вакансиями
        """
        print()
        info = []
        for params_vacancy in top_salary[int(number_of_vacancies)]:
            for key, val in params_vacancy.items():
                info.append("{0}: {1}".format(key, val))
        return '\n'.join(info)
