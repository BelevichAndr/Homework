from django.contrib import admin
from .models import *


class TasksAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(Student)
class RegisterInfo(admin.ModelAdmin):
    list_display = ("firstname", "lastname")


@admin.register(Book)
class RegisterInfo(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(Tasks, TasksAdmin)
