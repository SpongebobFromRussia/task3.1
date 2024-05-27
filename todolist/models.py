from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Название дела', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Текущие дела'

    def __str__(self):
        return self.title
