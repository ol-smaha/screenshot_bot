from django.core.exceptions import ValidationError
from django.db import models


class Bot(models.Model):
    name = models.CharField(default='SqreenshotBot',
                            max_length=32)

    def save(self, *args, **kwargs):
        if not self.pk and Bot.objects.exists():
            raise ValidationError('There is can be only one Bot instance')
        return super(Bot, self).save(*args, **kwargs)

