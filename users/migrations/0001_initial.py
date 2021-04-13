# Generated by Django 3.1.7 on 2021-04-13 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_type', models.CharField(choices=[('ADMIN', 'ADMIN'), ('TEACHER', 'TEACHER'), ('MENTOR', 'MENTOR'), ('STUDENT', 'STUDENT'), ('CLIENT', 'CLIENT')], default='CLIENT', max_length=20, verbose_name='Тип пользователя')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('telegram', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telegram')),
                ('github', models.URLField(blank=True, max_length=150, null=True, verbose_name='Github')),
                ('instagram', models.CharField(blank=True, max_length=150, null=True, verbose_name='Instagram')),
                ('image', models.ImageField(blank=True, max_length=254, null=True, upload_to='media')),
                ('coins', models.IntegerField(blank=True, null=True, verbose_name='Geek coins')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date of join')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone number')),
                ('birthday', models.DateField(blank=True, max_length=20, null=True, verbose_name='Birthday')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='MentorComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentor', to=settings.AUTH_USER_MODEL)),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commented_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий к ментору',
                'verbose_name_plural': 'Комментарий к ментору',
                'ordering': ['created'],
            },
        ),
    ]
