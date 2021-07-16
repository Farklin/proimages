from django.db import models





class Catalog(models.Model):
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    url = models.CharField(max_length=255, verbose_name = 'URL Сайта', blank=True, null=False)


class FieldCatalog(models.Model):
    class Meta:
        verbose_name = 'Поле каталога'
        verbose_name_plural = 'Поля каталога'

    location = models.CharField(max_length=500, verbose_name = 'Расположение элемента', default=None, blank=True, null=True)
    value = models.CharField(max_length=500, verbose_name = 'Название поля', default=None, blank=True, null=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

class Company(models.Model):
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    url = models.CharField(max_length=255, verbose_name = 'URL сайта')
    phone = models.CharField(max_length=255, verbose_name = 'Телефон сайта', default=None, blank=True, null=True)
    time = models.CharField(max_length=255, verbose_name = 'Часы работы', default=None, blank=True, null=True)
    adress = models.CharField(max_length=255, verbose_name = 'Адресс компании', default=None, blank=True, null=True)
    email = models.CharField(max_length=255, verbose_name = 'Email', default=None, blank=True, null=True)
    name_firm = models.CharField(max_length=255, verbose_name = 'Название фирмы', default=None, blank=True, null=True)
    name_person = models.CharField(max_length=255, verbose_name = 'Ваше имя', default=None, blank=True, null=True)

