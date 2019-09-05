from django.db import models


class Phone(models.Model):
    model = models.CharField(verbose_name='Модель', max_length=100, db_index=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    op_system = models.CharField(blank=True, verbose_name='Операционная система', max_length=50)
    ram = models.PositiveIntegerField(blank=True, verbose_name='Оперативная память')
    dpi = models.PositiveIntegerField(blank=True, verbose_name='Число пикселей на дюйм')
    double_cam = models.BooleanField(verbose_name='двойная камера')
    cpu = models.CharField(blank=True, verbose_name='Процессор', max_length=150)
    resolution = models.CharField(verbose_name='Разрешение экрана', max_length=50)
    fm_radio = models.BooleanField(verbose_name='FM-Радио')
    additionally = models.TextField(blank=True, verbose_name='Дополнительно')
    image = models.ImageField(blank=True, height_field=None, width_field=None)

    def __str__(self):
        return f'{self.model}'


