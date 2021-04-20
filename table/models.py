from django.db import models

# Create your models here.
from courses.models import Lesson
from users.models import User


class TableModel(models.Model):

    class Meta:
        verbose_name = 'Посещаемость - Успеваемость'
        verbose_name_plural = 'Посещаемость - Успеваемость'
        ordering = ['id']

    is_here = models.BooleanField(default=None, blank=True, null=True, verbose_name='Посещаемость')
    score = models.IntegerField(blank=True, null=True, default=None, verbose_name='Оценка за ДЗ')
    student = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='table_student', verbose_name='Студент')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name='lesson', verbose_name='Урок')
    date_of_lesson = models.DateField()

