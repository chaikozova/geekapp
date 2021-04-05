# Generated by Django 3.1.7 on 2021-04-01 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentor', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='commented_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий к ментору',
                'verbose_name_plural': 'Комментарий к ментору',
                'ordering': ['created'],
            },
        ),
    ]