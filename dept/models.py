from django.db import models


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


# Описание смен
class Change(models.Model):
    class Meta:
        verbose_name = "Описание смены"
        verbose_name_plural = "Описание смен"

    schedule = models.ForeignKey(Schedule)
    title = models.CharField(max_length=50)
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
