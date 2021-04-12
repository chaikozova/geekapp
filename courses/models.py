from django.contrib.postgres.fields import ArrayField
from django.db import models
from users.models import User


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    logo = models.ImageField(upload_to='media', max_length=240, blank=True, null=True)
    title = models.CharField(max_length=240)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    # @property
    # def levels_count(self):
    #     levels = Level.objects.filter(course=self.pk)
    #     return levels.count()


class Level(models.Model):
    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
    title = models.CharField(max_length=150, null=True)
    level_number = models.IntegerField()
    teacher = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='teacher')
    image = models.ImageField(upload_to='media',
                              max_length=240, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                               null=True, related_name='level')

    def __str__(self):
        return self.title

    # @property
    # def lessons_count(self):
    #     lessons = Lesson.objects.filter(level=self.pk)
    #     return lessons.count()


class GroupLevel(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    month = models.ForeignKey(Level, on_delete=models.CASCADE,
                              null=False, blank=True,
                              related_name='group_level')
    students = models.ForeignKey(User, null=True, blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='group_students')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    title = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='lessons')
    video_url = models.URLField(null=True, blank=True)
    material_url = ArrayField(models.CharField(max_length=250, null=True, blank=True), size=5, null=True, blank=True)

    def __str__(self):
        return self.title
