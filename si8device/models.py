from django.db import models
from django.contrib.auth.models import User

'''
Deportament -> Sector -> Equipment -> Register -> PollResult
'''


class Departament(models.Model):
    """ цех """
    class Meta:
        db_table = 'si8_departament'
        verbose_name = "Цех"
        verbose_name_plural = "Цех"

    departament_name = models.CharField(max_length=60)

    def __str__(self):
        result = ('%s' % self.departament_name)
        return result


class Sector(models.Model):
    """ участок """
    class Meta:
        db_table = 'si8_sector'
        verbose_name = "Участок"
        verbose_name_plural = "Участок"

    sector_departament = models.ForeignKey(Departament)
    sector_name = models.CharField(max_length=60)

    def __str__(self):
        result = ('%s-%s' % (self.sector_departament, self.sector_name))
        return result


class Equipment(models.Model):
    """  оборудование """
    class Meta:
        db_table = 'si8_equipment'
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

    equipment_sector = models.ForeignKey(Sector)   # участок
    equipment_enable = models.BooleanField()
    equipment_name = models.CharField(max_length=60)

    def __str__(self):
        result = ('%s - %s' % (self.equipment_sector, self.equipment_name))
        return result


class Register(models.Model):
    """ устройство - регистр для опроса """
    class Meta:
        db_table = 'si8_register'
        verbose_name = "Устройство"
        verbose_name_plural = "Устройство"

    register_equipment = models.ForeignKey(Equipment)    # привязка к оборудованию
    register_enable = models.BooleanField()              # разрешение опроса
    register_name = models.CharField(max_length=200)     # имя параметра для отображения
    register_addr = models.IntegerField()                # адрес устройства
    register_regname = models.CharField(max_length=60)   # имя регистра

    # registr_protocol = models.CharField(max_length=20)
    # registr_addrlen = models.IntegerField()

    def __str__(self):
        # count = Register.objects.filter(id=self.id).count()
        count = self.pollresult_set.filter(pollresult_register=self.id).count()
        result = ('%s-%s, addr = %s, reg = %s, count = %s' % (self.register_equipment, self.register_name,
                                                              self.register_addr, self.register_regname, count))
        return result


class PollResult(models.Model):
    """ результат опроса """
    class Meta:
        db_table = 'si8_pollresult'
        verbose_name = "Результат опроса"
        verbose_name_plural = "Результат опроса"
    pollresult_register = models.ForeignKey(Register)
    pollresult_value = models.FloatField()
    # pollresult_time = models.DateTimeField()
    pollresult_time = models.CharField(max_length=60)

    def __str__(self):
        result = ('%s - %s:%s' % (self.pollresult_register, self.pollresult_time, self.pollresult_value))
        return result
