# Generated by Django 3.0.4 on 2020-05-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0026_historyevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyevent',
            name='source_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
