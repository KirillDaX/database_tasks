# Generated by Django 2.2.4 on 2019-08-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='additionally',
            field=models.TextField(blank=True, verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='cpu',
            field=models.CharField(blank=True, max_length=150, verbose_name='Процессор'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='dpi',
            field=models.PositiveIntegerField(blank=True, verbose_name='Число пикселей на дюйм'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='phone',
            name='op_system',
            field=models.CharField(blank=True, max_length=50, verbose_name='Операционная система'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='ram',
            field=models.PositiveIntegerField(blank=True, verbose_name='Оперативная память'),
        ),
    ]
