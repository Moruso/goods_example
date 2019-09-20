from django.db import models


# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
