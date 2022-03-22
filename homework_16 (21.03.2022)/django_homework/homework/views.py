from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    if request.method == "POST":
        result = len(request.POST.get("author_first_name"))
        output_string = f"Длина имени составляет {result} символов"
        return HttpResponse(f"<h1>{output_string}</h1>")
    return render(request, "first.html")


def second(request):
    if request.method == "POST":
        age = request.POST.get("age")
        if age == "0-17":
            output_string = "В доступе отказано"
            return HttpResponse(f"<h1>{output_string}</h1>")
        output_string = "Добро пожаловать"
        return HttpResponse(f"<h1>{output_string}</h1>")
    return render(request, "second.html")


def third(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        comment_length = len(comment)
        vowels_eng = ["a", "e","i", "o", "u", "y"]
        vowels_ru = ["а","е","ё", "и", "у", "ы", "э", "ю", "я", "о"]
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


def sixth(request):
    if request.method == "POST":
        name = request.POST.get("author_first_name")
        context = {
            "name": name
        }
        return render(request, "sixth.html", context=context)
    return render(request, "first.html")