from django.db import models

# Create your models here.

class Diler(models.Model):
    title = models.CharField('Наименование дилера', max_length=50)
    # DC = models.ManyToOneRel('Дилерский центр')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'
