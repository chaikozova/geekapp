from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    address = models.CharField("Адрес", max_length=250)
    subaddress = models.CharField("Дополнение к адресу", max_length=250, null=True, blank=True)
    city = models.CharField("Город", max_length=50)
    phone_number = models.CharField("Номер телефона", max_length=100)
    url = models.CharField("Сайт", max_length=150, blank=True, null=True)


