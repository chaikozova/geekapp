from django.db import models
from users.models import User


class Request(models.Model):

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', null=True)
    month = models.CharField(verbose_name='Месяц', max_length=50, blank=True, null=True)
    category = models.CharField(verbose_name='Категория', max_length=100, blank=True, null=True)
    group_number = models.CharField(verbose_name='Номер группы', max_length=100, blank=True, null=True)
    course_program = models.CharField(verbose_name='Программа курса', max_length=100, blank=True,
                                      null=True)
    teacher = models.CharField(verbose_name='Учитель', max_length=100, blank=True, null=True)
    problem_title = models.TextField(verbose_name='Название запроса')
    problem_description = models.TextField(verbose_name='Описание запроса')
    file = models.FileField(upload_to='media', verbose_name='Прикрепите файл', blank=True, null=True)

    @property
    def notification_mentors(self):
        not_users = User.objects.filter(user_type='MENTOR')
        return not_users.filter(group_students__month__level_number__gt=self.month)


class Notification(models.Model):

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    recipients = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_recipients', null=True)
    message = models.CharField(verbose_name='Текст уведомления', max_length=50, blank=True, null=True)
    type = models.CharField(verbose_name='Категория уведолмения', max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    recieved_date = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(verbose_name='Прочитано', blank=True, null=True, default=None)
    is_match = models.BooleanField(verbose_name='Программа курса', max_length=100, blank=True,
                                   null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_sender', null=True)
    is_read_by_mentor = models.BooleanField(default=None, null=True)


