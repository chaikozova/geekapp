

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('subaddress', models.CharField(blank=True, max_length=250, null=True, verbose_name='Дополнение к адресу')),
                ('city', models.CharField(max_length=50, verbose_name='Город'))
                ('phone_number_o', models.CharField(max_length=100, verbose_name='Номер телефона_o')),
                ('phone_number_megacom', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер телефона_megacom')),
                ('phone_number_beeline', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер телефона_beeline')
           
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
