from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


def main_page(request):
    hw_name_list = ["homework_16/",
                    "homework_17/",
                    ]
    context = {
        "hw_name_list": hw_name_list
    }
    return render(request, "main.html", context=context)


def main_hw_16(request):
    hw_name_list = ["first/",
                    "second/",
                    "third/",
                    "sixth/",
                    ]
    context = {
        "hw_name_list": hw_name_list
    }
    return render(request, "main.html", context=context)


def main_hw_17(request):
    hw_name_list = ["first/",
                    "auto_first/",
                    "add_customer/",
                    ]
    context = {
        "hw_name_list": hw_name_list
    }
    return render(request, "main.html", context=context)


def first_hw16(request):
    if request.method == "POST":
        result = len(request.POST.get("author_first_name"))
        output_string = f"Длина имени составляет {result} символов"
        return HttpResponse(f"<h1>{output_string}</h1>")
    return render(request, "first.html")


def second_hw16(request):
    if request.method == "POST":
        age = request.POST.get("age")
        if age == "0-17":
            output_string = "В доступе отказано"
            return HttpResponse(f"<h1>{output_string}</h1>")
        output_string = "Добро пожаловать"
        return HttpResponse(f"<h1>{output_string}</h1>")
    return render(request, "second.html")


def third_hw16(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        comment_length = len(comment)
        vowels_eng = ["a", "e", "i", "o", "u", "y"]
        vowels_ru = ["а", "е", "ё", "и", "у", "ы", "э", "ю", "я", "о"]
        vowels = vowels_ru + vowels_eng
        vowels_counter = 0
        consonants_counter = 0

        for letter in comment:
            if letter.lower() in vowels:
                vowels_counter += 1
            else:
                consonants_counter += 1

        output_string = f"Длина комментария - {comment_length} символов. {vowels_counter} гласных," \
                        f" {consonants_counter} согласных"
        return HttpResponse(f"<h1>{output_string}</h1>")
    return render(request, "third.html")


def sixth_hw16(request):
    if request.method == "POST":
        name = request.POST.get("author_first_name")
        context = {
            "name": name
        }
        return render(request, "sixth.html", context=context)
    return render(request, "first.html")


def first_hw17(request):
    if request.method == "POST":
        form = InformationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            string = ""
            for key in data:
                string += f"{data.get(key)}|"
            print(string)
            return render(request, "hw_17/first_task.html")
        print(form.errors)
        return HttpResponse("ошибка")
    return render(request, "hw_17/first_task.html")


def auto_first_hw17(request):
    if request.method == "GET":
        context = {'form': InformationForm()}
        return render(request, "hw_17/auto_first_task.html", context=context)
    if request.method == "POST":
        form = InformationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            string = ""
            for key in data:
                string += f"{data.get(key)}|"
            print(string)
            context = {'form': InformationForm()}
            return render(request, "hw_17/auto_first_task.html", context=context)
        print(form.errors)
        return HttpResponse("ошибка")


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Сохранено")
            except:
                return HttpResponse("Ошибка")

            context = {
                "form": CustomerForm()
            }
            return render(request, "hw_17/add_customer_form.html", context=context)
    else:
        form = CustomerForm()
        context = {
            "form": form
        }
    return render(request, "hw_17/add_customer_form.html", context=context)
