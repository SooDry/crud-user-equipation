from django.utils.timezone import now

from django.db import models


# Create your models here.
class User(models.Model):
    identification = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    save_user = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.name + " " + self.last_name, self.identification)
