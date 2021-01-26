from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    sprice = models.IntegerField()
    cprice = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to='items', default='default.png', blank=True)

    def __str__(self):
        return self.name