from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from .models import Tasks, Customer
from rest_framework.views import APIView
from .forms import TasksForm, CustomerForm


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


def home21(request):
    return HttpResponse("<h1>Home page</h1>")


class HomeWork21View(View):
    def get(self, request):
        form = CustomerForm()
        context = {
            "form": form
        }
        return render(request, "hw21form.html", context=context)

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            print(Customer.objects.all())
            return redirect("home21")
        return form.errors

