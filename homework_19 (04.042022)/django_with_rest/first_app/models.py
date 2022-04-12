from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
