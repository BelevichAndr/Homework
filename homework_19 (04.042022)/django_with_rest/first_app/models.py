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


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    page_count = models.PositiveIntegerField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
