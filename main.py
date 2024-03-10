from scr.UserInteraction import UserInteraction


def main():
    user_input = input("Пожалуйста, напишите название вакансии для поиска: ")

    while True:
        users_salary = input("Напишите зарплату, если хотите\n"
                             "посмотреть вакансии с зарплатой:\n")
        if users_salary.isdigit():
            break
        print("\nПожалуйста, введите номер или введите 'Enter' \n")

    user = UserInteraction(user_input)

    while True:
        users_city = input("Теперь вам нужно ввести желаемый город работы :\n").capitalize()
        if users_city.isalpha():
            break
        print("\nЯ ничего не знаю об этом городе.\n")

    user.sorted_salary(user.all_vacancy, int(users_salary), users_city)
    user.get_top_vacancies(user.sort_salary)

    user.make_info(user.top_salary)

    while True:
        number_vacancy = input("Выберите номер топовой вакансии\n"
                               "если вы хотите увидеть больше: ")
        if number_vacancy.isdigit():
            break

    print(user.last_info(user.vacancies_list, number_vacancy))


if __name__ == '__main__':
    main()
