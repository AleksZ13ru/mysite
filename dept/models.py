from django.db import models
from django.utils import timezone
import datetime, calendar
import copy

# Персонал
class People(models.Model):
    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

    family = models.CharField(max_length=100)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30, blank=True, null=True)
    function = models.ForeignKey('Function')
    schedule = models.ForeignKey('Schedule', blank=True, null=True)
    birtday = models.DateField(blank=True, null=True)
    dayofwork = models.DateField(blank=True, null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        fio = '%s %s.%s. - %s' % (
            self.family,
            self.firstname[0],
            self.secondname[0],
            self.function,
            )
        return fio

    def fio(self):
        fio = '%s %s.%s.' % (
            self.family,
            self.firstname[0],
            self.secondname[0],
            )
        return fio


# Должность
class Function(models.Model):
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True, null=True)
    fileurl = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title


# Отпуска
class Holiday(models.Model):
    class Meta:
        verbose_name = "Отпуск"
        verbose_name_plural = "Отпуска"

    TYP_CHOICES = (
        (u'план', u'план'),
        (u'факт', u'факт'),
    )
    people = models.ForeignKey('People')
    typ = models.CharField(max_length=4, choices=TYP_CHOICES)
    year = models.IntegerField()
    startday = models.DateField()
    lenght = models.IntegerField()
    stopday = models.DateField()

    def __str__(self):
        return "%s %s - %s (%s)" % (People.fio(self.people),
                                    self.year, self.startday, self.typ)

    @staticmethod
    def modify_schedule(year=None, month=None, persons=None):
        result_return = {}
        out_persons = []

        list_holiday = Holiday.objects.filter(year=year)
        for holiday in list_holiday:
            for person in persons['persons']:
                if holiday.people.fio() == person['person']:
                    for i in range(0, holiday.lenght):
                        person['data'][holiday.startday.day+i-1] = 'h'
                out_persons.append(person)

        result_return['persons'] = out_persons
        result_return['schedules'] = persons['schedules']
        result_return['count_day'] = persons['day_in_month']
        return result_return

    @staticmethod
    def modify_schedule_v3(year=None, month=None, persons=None):
        # persons = {'fio':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'd', 'n', ...]}
        result_return = {}
        out_persons = []

        list_holiday = Holiday.objects.filter(year=year)
        for holiday in list_holiday:
            for person in persons['persons']:
                l_fio = copy.deepcopy(person['fio'])
                l_schedule = copy.deepcopy(person['schedule'])
                l_data = copy.deepcopy(person['data'])
                if holiday.people.fio() == l_fio:
                    for i in range(0, holiday.lenght):
                        l_data[holiday.startday.day+i-1] = 'h'
                out_persons.append({'fio': l_fio, 'schedule': l_schedule, 'data': l_data})

        result_return['persons'] = out_persons
        result_return['schedules'] = persons['schedules']
        result_return['day_in_month'] = persons['day_in_month']
        return result_return

    @staticmethod
    def modify_schedule_v2(year=None, month=None, persons=None):
        # persons = {'person':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'd', 'n', ...]}
        result = []
        #out_persons = persons

        # list_holiday = Holiday.objects.filter(year=year)

        for person, data in persons['persons']:
            t_person = person['person']
            t_data = person['data']
            t_schedule = person['schedule']
            list_holiday = Holiday.objects.filter(year=year).filter(startday__month=month)
            for holiday in list_holiday:
                if holiday.people.fio() == t_person:
                    for i in range(0, holiday.lenght):
                        t_data[holiday.startday.day+i-1] = 'h'

            result.append({'person': t_person, 'schedule': t_schedule, 'data': t_data})
        # result_return['persons'] = out_persons
        # result_return['schedules'] = persons['schedules']
        # result_return['day_in_month'] = persons['day_in_month']

        return result


# График работы
class Schedule(models.Model):
    class Meta:
        verbose_name = "График работы"
        verbose_name_plural = "Графики работы"

    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    startday = models.DateField()

    def __str__(self):
        return "%s" % (self.title)

    @staticmethod
    def today():
        schedules = Schedule.objects.all()
        std = None
        for schedule in schedules:
            t = (timezone.now().toordinal()-schedule.startday.toordinal()) % 4
            if t == 0:
                std = schedule.startday
        if std is None:
            return None
        else:
            return Schedule.objects.filter(startday=std)

    @staticmethod
    def itermonthdates(year=None, month=None):
        """
        Получение массива кодов(d - день, n - ночь, w - выходной) для указанного месяца
        для смен выбранных по фильтру: (.filter(title__icontains='№'))

        :param year: 2016
        :param month: 11 = декабрь
        :return: format=<class 'list'>: [{'person': ['Иняшев О.Ю.', 'Тимофеев Е.Л.'],
                                            name': 'Cмена №1', 'data': ['w', 'w', 'd', 'n', ...]},
                                        {'person': ['Володин Ю.А.', 'Ганин С.В.'],
                                            'name': 'Смена №2', 'data': ['n', 'w', 'w', 'd', ...]},
                                        {'person': ['Петров А.Б.', 'Пронин П.И.'],
                                            'name': 'Смена №3', 'data': ['d', 'n', 'w', 'w', ...]},
                                        {'person': ['Игошев С.О.', 'Сундиков А.В.'],
                                            'name': 'Смена №4', 'data': ['w', 'd', 'n', 'w', ...]}]

        """
        if year is None or month is None:
            return None
        # schedules = Schedule.objects.all()
        schedules = Schedule.objects.filter(title__icontains='№')
        schedules_return = []

        for schedule in schedules:
            schedule_return = {}
            schedule_data = []
            changes = Change.objects.filter(schedule=schedule)
            mass = []
            for change in changes:
                mass.append(change.title)
            my_cal = calendar.Calendar(firstweekday=0)
            for d in my_cal.itermonthdates(year, month):
                if d.month == month:
                    t = (d.toordinal() - schedule.startday.toordinal()) % len(mass)
                    schedule_data.append(mass[t])
            schedule_return['name'] = schedule.title
            schedule_return['data'] = schedule_data
            persons = People.objects.filter(schedule=schedule)
            person_array = []
            for person in persons:
                person_array.append(person.fio())
            schedule_return['person'] = person_array
            schedules_return.append(copy.deepcopy(schedule_return))
        return schedules_return

    @staticmethod
    def itermonthdates_v2(year=None, month=None):
        """
        Получение массива кодов(d - день, n - ночь, w - выходной) для указанного месяца
        для смен выбранных по фильтру: (.filter(title__icontains='№'))

        :param year: 2016
        :param month: 11 = декабрь
        :return: format=<class 'list'>: [{'person': ['Иняшев О.Ю.', 'Тимофеев Е.Л.'],
                                            name': 'Cмена №1', 'data': ['w', 'w', 'd', 'n', ...]},
                                        {'person': ['Володин Ю.А.', 'Ганин С.В.'],
                                            'name': 'Смена №2', 'data': ['n', 'w', 'w', 'd', ...]},
                                        {'person': ['Петров А.Б.', 'Пронин П.И.'],
                                            'name': 'Смена №3', 'data': ['d', 'n', 'w', 'w', ...]},
                                        {'person': ['Игошев С.О.', 'Сундиков А.В.'],
                                            'name': 'Смена №4', 'data': ['w', 'd', 'n', 'w', ...]}]

        :return: format=<class 'list'>: [{'person':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'd', 'n']},
                                         {'person':'Володин Ю.А.','schedule':'Cмена №2', 'data':['w', 'w', 'd', 'n']},
                                         {'person':'Петров А.Б.', 'schedule':'Cмена №3', 'data':['w', 'w', 'd', 'n']},
                                         {'person':'Игошев С.О.', 'schedule':'Cмена №4', 'data':['w', 'w', 'd', 'n']}]


        """
        if year is None or month is None:
            return None
        # result = {}
        result = {'schedules': [], 'day_in_month': calendar.monthrange(year, month)[1], 'persons': []}  # структура
        # schedules = Schedule.objects.all()
        schedules = Schedule.objects.filter(title__icontains='№')

        for schedule in schedules:
            result['schedules'].append(schedule.title)
            # people = {}
            schedule_data = []
            changes = Change.objects.filter(schedule=schedule)
            schedule_data_bloc = []
            for change in changes:
                schedule_data_bloc.append(change.title)
            # result['count_day'] = len(schedule_data_bloc)
            my_cal = calendar.Calendar(firstweekday=0)
            for d in my_cal.itermonthdates(year, month):
                if d.month == month:
                    t = (d.toordinal() - schedule.startday.toordinal()) % len(schedule_data_bloc)
                    schedule_data.append(copy.deepcopy(schedule_data_bloc[t]))
            # people['schedule'] = schedule.title
            # people['data'] = schedule_data
            persons = People.objects.filter(schedule=schedule)
            for person in persons:
                # people['person'] = person.fio()
                # people['schedule'] = schedule.title
                # people['data'] = schedule_data
                result['persons'].append({'fio': person.fio(), 'schedule': schedule.title, 'data': schedule_data})
        return result


# Описание смен
class Change(models.Model):
    class Meta:
        verbose_name = "Описание смены"
        verbose_name_plural = "Описание смен"

    schedule = models.ForeignKey(Schedule)
    title = models.CharField(max_length=50)
    number = models.IntegerField()
    starttime = models.TimeField()
    stoptime = models.TimeField()

    def __str__(self):
        return self.title


# Отгулы и выходные
class Weekend(models.Model):
    class Meta:
        verbose_name = "Отгулы и выходные"
        verbose_name_plural = "Отгулы и выходные"

    TYP_MOTIVE = (
        (u'Служеб.', u'Служебное задание'),
        (u'Семейн.', u'Семейные обстоятельства'),
        (u'Другое ', u'Другое'),
    )
    TYP_CHOICES = (
        (u'Выходной', u'Выходной'),
        (u'Отгул', u'Отгул'),
        (u'Без содержания', u'Без содержания'),
    )
    people = models.ForeignKey('People')
    typ = models.CharField(max_length=16, choices=TYP_CHOICES)
    motive = models.CharField(max_length=8, choices=TYP_MOTIVE)
    datestart = models.DateField()
    timestart = models.TimeField()
    stoptime = models.TimeField()

    def __str__(self):
        return '%s был в: %s - %s числа по причине: %s  ' % (
            People.fio(self.people),
            self.typ,
            self.datestart,
            self.motive)
