from django.db import models



class QuestionAndAnswer(models.Model):
    class Meta:
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы-Ответы'

    question_text = models.CharField(max_length=250, null=True, blank=True)
    answer_text = models.TextField(null=True, blank=True)


class ToJoinTheCourse(models.Model):
    class Meta:
        verbose_name = 'Запись на курс'

    COURSES = (
        ('android', 'Android-разработка'),
        ('backend', 'Backend-разработка'),
        ('front', 'Frontend-разработка'),
        ('design', 'UI/UX design'),
        ('ios', 'iOS-разработка'),
    )

    course = models.CharField(choices=COURSES, verbose_name='Курс', max_length=50)
    name_and_surname = models.CharField(max_length=50, verbose_name='Имя и фамилия')
    telephone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
