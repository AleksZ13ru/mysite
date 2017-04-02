from django.db import models
from django.utils import timezone
import calendar
import datetime
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
    lenght = models.IntegerField(default=14)
    stopday = models.DateField(blank=True, null=True)

    def save(self, *args, **kw):
        # self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
        self.stopday = self.startday + datetime.timedelta(days=self.lenght - 1)
        super(Holiday, self).save(*args, **kw)

    def __str__(self):
        return "%s %s - %s (%s)" % (People.fio(self.people),
                                    self.year, self.startday, self.typ)

    @staticmethod
    def modify_schedule(year=None, month=None, persons=None):
        """
        Производится поиск отпусков для persons['fio_id'], и произвдится замена полей persons['data'][n] на 'h'
        'h' - код для отпуска
        :param year: год
        :param month: месяц
        :param persons: = {'fio_id':16, 'fio':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'd', 'n', ...]}
        :return: = {'fio_id':16, 'fio':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'h', 'h', ...]}
        """

        result_return = {}
        out_persons = copy.deepcopy(persons['persons'])

        for person in persons['persons']:
            holidays = Holiday.objects.filter(people_id=person['fio_id'])
            for holiday in holidays:
                d_start = holiday.startday.toordinal()
                d_end = d_start + holiday.lenght
                d_mount_start = datetime.date(year, month, 1).toordinal()
                d_mount_end = datetime.date(year, month + 1, 1).toordinal()

                l_fio = copy.deepcopy(person['fio'])
                l_schedule = copy.deepcopy(person['schedule'])
                l_data = copy.deepcopy(person['data'])
                l_fio_id = copy.deepcopy(person['fio_id'])

                # месяц   |-----|
                # отпуск  | --  |
                if d_start >= d_mount_start and d_end <= d_mount_end:
                    pass
                    p = out_persons.index(person)  # номер позиции персоны в списке, для модификации
                    a = holiday.startday.day
                    out_persons.pop(p)
                    for i in range(a, a + holiday.lenght):
                        l_data[i - 1] = 'h'
                    out_persons.insert(p, {'fio': l_fio, 'schedule': l_schedule, 'data': l_data, 'fio_id': l_fio_id})

                # месяц   |  -----|
                # отпуск  | --    |
                elif d_start < d_mount_start and d_end > d_mount_start:
                    # начинается до этого месяца
                    p = out_persons.index(person)  # номер позиции персоны в списке, для модификации
                    out_persons.pop(p)
                    a = 1
                    for i in range(a, a + d_end - d_mount_start):
                        l_data[i - 1] = 'h'
                    out_persons.insert(p, {'fio': l_fio, 'schedule': l_schedule, 'data': l_data, 'fio_id': l_fio_id})

                # месяц   |-----  |
                # отпуск  |    -- |
                elif d_start < d_mount_end and d_end > d_mount_end:
                    # после
                    p = out_persons.index(person)  # номер позиции персоны в списке, для модификации
                    out_persons.pop(p)
                    # out_persons.remove(person)
                    try:
                        a = holiday.startday.day
                        for i in range(a, a + holiday.lenght):
                            l_data[i - 1] = 'h'
                    except IndexError:
                        pass
                    # out_persons.append({'fio': l_fio, 'schedule': l_schedule, 'data': l_data, 'fio_id': l_fio_id})
                    out_persons.insert(p, {'fio': l_fio, 'schedule': l_schedule, 'data': l_data, 'fio_id': l_fio_id})
                # месяц   |-----    |
                # отпуск  |      -- |
                elif d_start > d_mount_end:
                    pass

                # месяц   |   -----|
                # отпуск  |--      |
                elif d_end < d_mount_start:
                    pass

                else:
                    pass

        result_return['persons'] = out_persons
        result_return['schedules'] = persons['schedules']
        result_return['day_in_month'] = persons['day_in_month']
        # result_return['fio_id'] = persons['fio_id']
        return result_return
        # ----------------------------------------------------------

    @staticmethod
    def modify_schedule_in5day(persons=None, day5=None):
        """
        Удаляет персоны у которых график работы не отличается от стандартного графика
        :param persons:
        :param day5:
        :return:
        """
        result_return = {}
        out_persons = []
        for person in persons['persons']:
            if person['data'] != day5:
                out_persons.append(person)
        result_return['persons'] = out_persons
        result_return['schedules'] = persons['schedules']
        result_return['day_in_month'] = persons['day_in_month']
        return result_return

    @staticmethod
    def day_in_year(year=None, month=None, day=None):
        d = datetime.date(year, month, day)
        result = d.toordinal()
        return result

    @staticmethod
    def modify_schedule_v2(year=None, month=None, persons=None):
        # persons = {'fio':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'd', 'n', ...]}
        result_return = {}
        t_persons = copy.deepcopy(persons['persons'])
        out_persons = []

        list_holiday = Holiday.objects.filter(year=year).filter(startday__month=month).filter(stopday__month=month)
        for holiday in list_holiday:
            for person in t_persons:
                l_fio = copy.deepcopy(person['fio'])
                l_schedule = copy.deepcopy(person['schedule'])
                l_data = copy.deepcopy(person['data'])
                if holiday.people.fio() == l_fio:
                    for i in range(0, holiday.lenght):
                        l_data[holiday.startday.day + i - 1] = 'h'
                t_persons.person = {'fio': l_fio, 'schedule': l_schedule, 'data': l_data}

        result_return['persons'] = out_persons
        result_return['schedules'] = persons['schedules']
        result_return['day_in_month'] = persons['day_in_month']
        return result_return


# График работы
class Schedule(models.Model):
    class Meta:
        verbose_name = "График работы"
        verbose_name_plural = "Графики работы"

    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    startday = models.DateField()

    def __str__(self):
        return self.title

    @staticmethod
    def today():
        schedules = Schedule.objects.all()
        std = None
        for schedule in schedules:
            t = (timezone.now().toordinal() - schedule.startday.toordinal()) % 4
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
        :return: format=<class 'list'>: [{'fio':'Иняшев О.Ю.', 'schedule':'Cмена №1', 'data':['w', 'w', 'd', 'n']},
                                         {'fio':'Володин Ю.А.','schedule':'Cмена №2', 'data':['w', 'w', 'd', 'n']},
                                         {'fio':'Петров А.Б.', 'schedule':'Cмена №3', 'data':['w', 'w', 'd', 'n']},
                                         {'fio':'Игошев С.О.', 'schedule':'Cмена №4', 'data':['w', 'w', 'd', 'n']}]


        """
        if year is None or month is None:
            return None
        # result = {}
        result = {'schedules': [], 'day_in_month': calendar.monthrange(year, month)[1], 'persons': []}  # структура
        schedules = Schedule.objects.all()
        # schedules = Schedule.objects.filter(title__icontains='№')

        for schedule in schedules:
            result['schedules'].append(schedule.title)
            schedule_data = []
            changes = Change.objects.filter(schedule=schedule)
            schedule_data_bloc = []
            for change in changes:
                schedule_data_bloc.append(change.title)
            my_cal = calendar.Calendar(firstweekday=0)
            for d in my_cal.itermonthdates(year, month):
                if d.month == month:
                    t = (d.toordinal() - schedule.startday.toordinal()) % len(schedule_data_bloc)
                    schedule_data.append(copy.deepcopy(schedule_data_bloc[t]))
            persons = People.objects.filter(schedule=schedule)
            for person in persons:
                result['persons'].append({'fio': person.fio(), 'schedule': schedule.title, 'data': schedule_data,
                                          'fio_id': person.id})
        return result

    @staticmethod
    def schedule_in5day(year=None, month=None):
        """
        возвращает data для обычной рабочей недели для организации фильтра.
        После проверки на наличие отпусков и т.д. все записи с стандартным графиком будут удалены из календаря

        :param year:
        :param month:
        :return: возвращает data для обычной рабочей недели 'data':['w', 'w', 'd', 'n']
        """
        schedule = Schedule.objects.filter(title__icontains='Дневная')[0]
        schedule_data = []
        changes = Change.objects.filter(schedule=schedule)
        schedule_data_bloc = []
        for change in changes:
            schedule_data_bloc.append(change.title)
        my_cal = calendar.Calendar(firstweekday=0)
        for d in my_cal.itermonthdates(year, month):
            if d.month == month:
                t = (d.toordinal() - schedule.startday.toordinal()) % len(schedule_data_bloc)
                schedule_data.append(copy.deepcopy(schedule_data_bloc[t]))
        return schedule_data

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


class MicroSchedule(models.Model):
    class Meta:
        verbose_name = "Подмена"
        verbose_name_plural = "Подмена"

    people = models.ForeignKey('People')
    schedule = models.ForeignKey('Schedule')
    startday = models.DateField()
    lenght = models.IntegerField(default=14)
    stopday = models.DateField(blank=True, null=True)

    def save(self, *args, **kw):
        self.stopday = self.startday + datetime.timedelta(days=self.lenght - 1)
        super(MicroSchedule, self).save(*args, **kw)

    def __str__(self):
        return "%s %s - %s (%s)" % (People.fio(self.people),
                                    self.schedule, self.startday, self.stopday)
