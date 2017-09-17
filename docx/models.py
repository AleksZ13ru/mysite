from django.db import models


# Служебная записка
class Memo(models.Model):
    class Meta:
        verbose_name = "Служебная записка"
        verbose_name_plural = "Служебные записки"

    number = models.IntegerField()  # номер
    title = models.CharField(max_length=100)    # заголовок
    # to_whom = models.CharField(max_length=100)  # кому
    to_whom = models.ForeignKey('PeopleToWhom')  # кому адресат = destination
    who = models.ForeignKey('PeopleWho', blank=True, null=True)  # исполнитель = executor
    day_create = models.DateField(blank=True, null=True)  # дата создания
    text = models.CharField(max_length=500, null=True)
    # event = models.ForeignKey('Event', blank=True, null=True)  # События
    # note = models.ForeignKey('Note', blank=True, null=True)  # Заметки
    # schedule = models.ForeignKey('Schedule', blank=True, null=True)

    def __str__(self):
        # Голубеву А.В. №123 от 12.08.2017 - запчасти для маркиров август
        memo = '%s №%s от %s - %s' % (
            self.to_whom,
            self.number,
            self.day_create,
            self.title,
        )
        return memo


class PeopleToWhom(models.Model):
    class Meta:
        verbose_name = "Адресат"
        verbose_name_plural = "Адресаты"
    name = models.CharField(max_length=100)    # заголовок

    def __str__(self):
        return self.name


class PeopleWho(models.Model):
    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"
    # name = models.CharField(max_length=100)    # заголовок
    family = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30, default='')
    second_name = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)  # должность
    phone_number = models.CharField(max_length=100, blank=True, null=True)  # номер телефона
    phone_mobile_number = models.CharField(max_length=100, blank=True, null=True)  # номер мобильного телефона

    def fio(self):
        fio = '%s %s.%s.' % (
            self.family,
            self.first_name[0],  # берем первую букву
            self.second_name[0]  # берем первую букву

        )
        return fio

    def __str__(self):
        fio = '%s %s.%s. - %s' % (
            self.family,
            self.first_name[0],   # берем первую букву
            self.second_name[0],  # берем первую букву
            self.position
        )
        return fio


# События
class Event(models.Model):
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    memo = models.ForeignKey('Memo')
    title = models.CharField(max_length=100)    # заголовок
    day_create = models.DateField()  # дата события
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        event = '%s: %s, %s' % (
            self.day_create,
            self.title,
            self.comment
        )
        return event


# Заметки
class Note(models.Model):
    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    memo = models.ForeignKey('Memo')
    title = models.CharField(max_length=100)    # заголовок
    day_create = models.DateField()  # дата события
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        note = '%s: %s, %s' % (
            self.day_create,
            self.title,
            self.comment
        )
        return note
