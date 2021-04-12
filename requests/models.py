from django.db import models
from users.models import User


# Create your models here.
class Request(models.Model):

    CATEGORY_TYPE = (
        ('1', 'Помогите с темой курса'),
        ('2', 'Помогите с домашним заданием'),
        ('3', 'Сходим пообедать'),
        ('4', 'Кто хочет в магазин'),
    )

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', null=True)
    month = models.CharField(verbose_name='Месяц', max_length=50, blank=True, null=True)
    category = models.CharField(choices=CATEGORY_TYPE, verbose_name='Категория', max_length=100, blank=True, null=True)
    group_number = models.CharField(verbose_name='Номер группы', max_length=100, blank=True, null=True)
    course_program = models.CharField(verbose_name='Программа курса', max_length=100, blank=True,
                                      null=True)
    teacher = models.CharField(verbose_name='Учитель', max_length=100, blank=True, null=True)
    problem_title = models.TextField(verbose_name='Название запроса')
    problem_description = models.TextField(verbose_name='Описание запроса')
    file = models.FileField(upload_to='media', verbose_name='Прикрепите файл', blank=True, null=True)


class Notification(models.Model):

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    CATEGORY_TYPE = (
        ('1', 'Помогите с темой курса'),
        ('2', 'Помогите с домашним заданием'),
        ('3', 'Сходим пообедать'),
        ('4', 'Кто хочет в магазин'),
    )

    recipients = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_recipients', null=True)
    notification_text = models.CharField(verbose_name='Текст уведомления', max_length=50, blank=True, null=True)
    type = models.CharField(choices=CATEGORY_TYPE, verbose_name='Категория уведолмения', max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(verbose_name='Прочитано', blank=True, null=True, default=None)
    is_match = models.BooleanField(verbose_name='Программа курса', max_length=100, blank=True,
                                   null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_sender', null=True)
