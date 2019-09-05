from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(data_for_slug):
    new_slug = slugify(data_for_slug, allow_unicode=True)
    return new_slug


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=150, db_index=True)
    price = models.PositiveIntegerField(blank=True)
    image = models.ImageField()
    release_date = models.DateField(blank=True)
    lte_exists = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.name}'
