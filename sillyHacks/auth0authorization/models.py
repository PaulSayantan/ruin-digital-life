from django.db import models

# Create your models here.


class CustomUser(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=256, blank=False, null=False)
    twitterId=models.TextField(blank=True,null=True)
    
class Thought(models.Model):
    id=models.AutoField(primary_key=True)
    thought=models.TextField()

class Image(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.TextField()

