from django.db import models


# Create your models here.


class Log(models.Model):
    user_id = models.IntegerField(primary_key=True)
    message = models.JSONField(default={"state": 0})


class TgUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    user_name = models.CharField(max_length=256, null=True, blank=True)
    phone = models.ImageField()

    def __str__(self):
        return self.first_name
