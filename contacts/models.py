
from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    address = models.CharField("Адрес", max_length=250)
    subaddress = models.CharField("Дополнение к адресу", max_length=250, null=True, blank=True)
    city = models.CharField("Город", max_length=50)
    phone_number_o = models.CharField("Номер телефона_o", max_length=100)
    phone_number_megacom = models.CharField("Номер телефона_megacom", max_length=100, null=True, blank=True)
    phone_number_beeline = models.CharField("Номер телефона_beeline", max_length=100, null=True, blank=True)


class QuestionAndAnswer(models.Model):
    class Meta:
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы-Ответы'
    question_text = models.CharField(max_length=250, null=True, blank=True)
    answer_text = models.TextField(null=True, blank=True)
