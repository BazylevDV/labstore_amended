from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserRegister  # Импортируй форму UserRegister

def sign_up_by_django(request: HttpRequest):
    # Псевдо-список существующих пользователей
    users = ["admin", "user1", "user2"]

    # Пустой словарь для передачи в context
    info = {}

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            # Проверка данных
            if password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif age < 18:
                info["error"] = "Вы должны быть старше 18"
            elif username in users:
                info["error"] = "Пользователь уже существует"
            else:
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()

    info["form"] = form
    return render(request, "fifth_task/registration_page.html", info)

def sign_up_by_html(request: HttpRequest):
    # Псевдо-список существующих пользователей
    users = ["admin", "user1", "user2"]

    # Пустой словарь для передачи в context
    info = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        # Проверка данных
        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
        elif not age or int(age) < 18:
            info["error"] = "Вы должны быть старше 18"
        elif username in users:
            info["error"] = "Пользователь уже существует"
        else:
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, "fifth_task/registration_page.html", info)