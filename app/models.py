from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_number = models.BigIntegerField(null=True)
    email = models.CharField(max_length=40, default='unknown@example.com')

    