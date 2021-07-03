from django.db import models
from datetime import datetime


# Create your models here.
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Заголовок', default=None, blank=True, null=True)
    path_image = models.FileField(upload_to='media', verbose_name = 'Изображение')
    date = models.DateTimeField(default=datetime.now, blank=True, verbose_name = 'Дата')