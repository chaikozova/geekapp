# Generated by Django 3.1.7 on 2021-04-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAndAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=250, null=True)),
                ('answer_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Вопрос-Ответ',
                'verbose_name_plural': 'Вопросы-Ответы',
            },
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]