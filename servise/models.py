from django.db import models

# Create your models here.

class D_c(models.Model):
    title = models.CharField('Наименование центра', max_length=50)
    # sail = models.F
    # repair = 'Ремонт'
    # s_zap = 'Склад запчастей'
    # s_avto = models.ManyToOneRel()

    def __str__(self):
        return f'Дилерский центр: {self.title}'

    class Meta:
        verbose_name = 'Дилерский центр'
        verbose_name_plural = 'Дилерские центры'

