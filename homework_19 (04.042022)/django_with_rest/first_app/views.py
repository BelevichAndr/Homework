from django.shortcuts import render
from rest_framework.response import Response
from .models import Tasks
from rest_framework.views import APIView


class TasksApi(APIView):
    def get(self, request):
        data_list = list(Tasks.objects.all().values())
        return Response({"tasks": data_list})

    def post(self, request):
        add_task = Tasks.objects.create(**request.data)
        data_list = list(Tasks.objects.all().values())
        return Response({"tasks": data_list})
