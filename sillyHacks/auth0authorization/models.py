from django.db import models

# Create your models here.


class CustomUser(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=256, blank=False, null=False)
    

