

def repack(input_dates):
    """

    :param input_dates: =[{'person': ['Иняшев О.Ю.', 'Тимофеев Е.Л.'],
                                            name': 'Cмена №1', 'data': ['w', 'w', 'd', 'n', ...]},
                                        {'person': ['Володин Ю.А.', 'Ганин С.В.'],
                                            'name': 'Смена №2', 'data': ['n', 'w', 'w', 'd', ...]},
                                        {'person': ['Петров А.Б.', 'Пронин П.И.'],
                                            'name': 'Смена №3', 'data': ['d', 'n', 'w', 'w', ...]},
                                        {'person': ['Игошев С.О.', 'Сундиков А.В.'],
                                            'name': 'Смена №4', 'data': ['w', 'd', 'n', 'w', ...]}]
    :return:
    """
    result_return = {}
    schedules = []  # массив
    persons = []  # массив
    count_day = 1
    for date in input_dates:
        schedules.append(date['name'])
        for person in date['person']:
            out_person = {'person': person, 'name_schedule': date['name'], 'data': date['data']}  # структура
            persons.append(out_person)
            count_day = len(date['data'])
    result_return['persons'] = persons
    result_return['schedules'] = schedules
    result_return['count_day'] = count_day
    return result_return


