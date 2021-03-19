from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .manager import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Base user model"""
    ADMIN = 'ADMIN'
    TEACHER = 'TEACHER'
    MENTOR = 'MENTOR'
    STUDENT = 'STUDENT'
    CLIENT = 'CLIENT'
    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (TEACHER, 'TEACHER'),
        (MENTOR, 'MENTOR'),
        (STUDENT, 'STUDENT'),
        (CLIENT, 'CLIENT'),
    )
    user_type = models.CharField(choices=USER_TYPE, default=CLIENT, verbose_name='Тип пользователя', max_length=20)
    email = models.EmailField(max_length=255, unique=True, db_index=True, verbose_name='Email')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='First name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last name')
    telegram = models.CharField(max_length=200, blank=True, null=True, verbose_name='Telegram')
    github = models.URLField(max_length=150, blank=True, null=True, verbose_name='Github')
    instagram = models.CharField(max_length=150, blank=True, null=True, verbose_name='Instagram')
    image = models.ImageField(upload_to='media', max_length=254, blank=True, null=True)
    coins = models.IntegerField(blank=True, null=True, verbose_name='Geek coins')
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date of join')
    is_staff = models.BooleanField(default=False, verbose_name='Is staff')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    phone_number = models.CharField(max_length=200, blank=True, null=True, verbose_name='Phone number')
    birthday = models.DateField(max_length=20, blank=True, null=True, verbose_name='Birthday')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


@receiver(post_save)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if issubclass(sender, User) and created:
        Token.objects.create(user=instance)


class Request(models.Model):
    MONTH_TYPE = (
        ('1', '1 месяц'),
        ('2', '2 месяц'),
        ('3', '3 месяц'),
        ('4', '4 месяц'),
        ('5', '5 месяц'),
        ('6', '6 месяц'),
        ('7', '7 месяц'),
    )

    CATEGORY_TYPE = (
        ('1', 'Помогите с темой курса'),
        ('2', 'Помогите с домашним заданием'),
        ('3', 'Сходим пообедать'),
        ('4', 'Кто хочет в магазин'),
    )

    PROGRAM_TYPE = (
        ('Back', 'Backend-разработчик'),
        ('Front', 'Frontend-разработчик'),
        ('IOS', 'iOS-разработчик'),
        ('Android', 'Android-разработка'),
        ('Ui/Ux', 'UX/UI Designer'),
        ('English', 'IT Английский'),
    )

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    student = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='student', null=True)
    month = models.CharField(choices=MONTH_TYPE, verbose_name='Месяц', max_length=50, blank=True, null=True)
    category = models.CharField(choices=CATEGORY_TYPE, verbose_name='Категория', max_length=100, blank=True, null=True)
    group_number = models.CharField(verbose_name='Номер группы', max_length=100, blank=True, null=True)
    course_program = models.CharField(choices=PROGRAM_TYPE, verbose_name='Программа курса', max_length=100, blank=True,
                                      null=True)
    teacher = models.CharField(choices=PROGRAM_TYPE, verbose_name='Учитель', max_length=100, blank=True, null=True)
    problem_title = models.TextField(verbose_name='Дайте название проблеме')
    problem_description = models.TextField(verbose_name='Опишите проблему')
    file = models.FileField(upload_to='media', verbose_name='Прикрепите файл', blank=True, null=True)
