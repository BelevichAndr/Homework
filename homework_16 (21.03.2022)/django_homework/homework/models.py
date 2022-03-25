from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname, self.lastname
