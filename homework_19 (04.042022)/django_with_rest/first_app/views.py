from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from .models import Tasks
from rest_framework.views import APIView
from .forms import TasksForm


class TasksApi(APIView):
    def get(self, request):
        data_list = list(Tasks.objects.all().values())
        return Response({"tasks": data_list})

    def post(self, request):
        add_task = Tasks.objects.create(**request.data)
        data_list = list(Tasks.objects.all().values())
        return Response({"tasks": data_list})


class HomeWorkView(View):

    def get(self, request):
        form = TasksForm()
        context = {
            "form": form
        }
        return render(request, "form.html", context=context)

    def post(self, request):
        form = TasksForm(request.POST)
        if form.is_valid():
            string = ""
            for key in form.cleaned_data:
                string += f"{form.cleaned_data.get(key)}|"
            print(string)
            return HttpResponse("Есть контакт")
        return form.errors


