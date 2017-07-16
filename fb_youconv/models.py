from django.db import models

class fb_user(models.Model):
    first_name = models.CharField(max_lenght = 30)
    last_name = models.CharField(max_length=30)
