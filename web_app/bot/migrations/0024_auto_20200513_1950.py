# Generated by Django 3.0.4 on 2020-05-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0023_auto_20200513_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmessage',
            name='date_create',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата створення'),
        ),
    ]
