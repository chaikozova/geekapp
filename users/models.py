from django.contrib.postgres.fields import ArrayField
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
    image = models.ImageField(upload_to='media', blank=True, null=True)
    coins = models.IntegerField(blank=True, null=True, verbose_name='Geek coins')
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date of join')
    is_staff = models.BooleanField(default=False, verbose_name='Is staff')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    phone_number = ArrayField(models.CharField(max_length=100, null=True, blank=True), size=5, null=True, blank=True)
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


class IsMentor(models.Model):
    class Meta:
        verbose_name = 'Стать ментором'
        verbose_name_plural = 'Стать ментором'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='is_mentor', null=True)
    is_mentor = models.BooleanField(default=None)
    blank_to_be_mentor = models.TextField()





