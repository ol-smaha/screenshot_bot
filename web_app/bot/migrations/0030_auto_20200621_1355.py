# Generated by Django 3.0.4 on 2020-06-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0029_auto_20200601_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyevent',
            name='description',
            field=models.TextField(unique=True, verbose_name='Подія'),
        ),
    ]
