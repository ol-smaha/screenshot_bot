# Generated by Django 3.0.4 on 2020-05-13 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_auto_20200513_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Зміст повідомлення')),
                ('status', models.CharField(choices=[('created', 'Створено'), ('send', 'Відправлено'), ('error', 'Помилка')], default=('created', 'Створено'), max_length=64, verbose_name='Статус')),
                ('to_all', models.BooleanField(default=False, verbose_name='Для всіх')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Дата створення')),
                ('date_send', models.DateTimeField(verbose_name='Дата відправлення')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.User', verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Повідомлення користувачу',
                'verbose_name_plural': 'Повідомлення користувачам',
                'ordering': ['-date_create'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Зміст повідомлення')),
                ('status', models.CharField(choices=[('open', 'Відритий'), ('closed', 'Закритий'), ('actual', 'Актуальний')], default=('open', 'Відритий'), max_length=64, verbose_name='Статус')),
                ('date_create', models.DateTimeField(verbose_name='Дата отримання')),
                ('parent_msg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.SendMessage', verbose_name="Зв'язане повідомлення")),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.User', verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Фідбек',
                'verbose_name_plural': 'Фідбеки',
                'ordering': ['-date_create'],
            },
        ),
    ]
