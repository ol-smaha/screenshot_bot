# Generated by Django 3.0.4 on 2020-05-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0025_auto_20200513_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=62)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Історична подія',
                'verbose_name_plural': 'Історичні події',
                'ordering': ['-year'],
            },
        ),
    ]
