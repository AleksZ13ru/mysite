from django.db import models


# Create your models here.
class Folder(models.Model):
    class Meta:
        verbose_name = "Папки"
        verbose_name_plural = "Папки"

    path = models.CharField(max_length=250)
    enable = models.BooleanField()

    def __str__(self):
        return self.path


class File(models.Model):
    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"

    name = models.CharField(max_length=50)
    path = models.CharField(max_length=250)
    parsing_status = models.IntegerField(default=0)  # 0 - еще не парсин,
                                                     # 1 - парсинг успешен,
                                                     # 2 - парсинг начат но не закончен
    hash = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.path, self.name)


