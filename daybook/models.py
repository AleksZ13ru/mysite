from django.db import models
from si8device.models import Equipment
from django.utils import timezone


class Memo(models.Model):
    class Meta:
        verbose_name = "Журнал передачи смен"
        verbose_name_plural = "Журнал передачи смен"

    equipment = models.ForeignKey(Equipment)  # название оборуования
    defect = models.TextField()  # неисправность
    working = models.TextField(blank=True, null=True)  # выполненая работа
    working_ok = models.BooleanField(default=False)  # ремонт завершен
    time_start = models.DateTimeField(default=timezone.now)  # время наступления неисправности
    time_ok = models.DateTimeField()  # время завершения ремонта
    # people = models.ManyToManyField()  # привлеченные люди

    def __str__(self):
        title = '%s - %s' % (
            self.equipment,
            self.defect
        )
        return title

    # @staticmethod
    # def downtime():  # получение ведомости простоев
    #     return 1

# add
# Модель ведомости простоев, должна автоматически формироваться из записей журнала.
#   может содержать отличный от журнала передачи смен, в итоговую ведомость попадают не все записи
# Модель передачи неисправного оборудования.- все без отметки о выполнении
# Скорее всего это даже не модели а представления записей журнала
