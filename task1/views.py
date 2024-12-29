from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserRegister  # Импортируем форму UserRegister
from django.db.models import Model
from .models import User, Product
from django.shortcuts import get_object_or_404, redirect
User: Model


def buy(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Здесь можно добавить логику для обработки покупки
    # Например, добавление товара в корзину или создание заказа
    return redirect('reagents')  # Перенаправляем обратно на страницу с реагентами


def labtorg(request):
    context = {
        'pagename': 'Лабораторное оборудование',
        'content': 'Добро пожаловать на страницу лабораторного оборудования!',
    }
    return render(request, 'fourth_task/labtorg.html', context)


def reagents(request):
    products = Product.objects.all()
    context = {
        'pagename': 'Реагенты',
        'content': 'Здесь вы можете найти наши реагенты.',
        'products': products,
    }
    return render(request, 'fourth_task/reagents.html', context)  #

def basket(request):
    cart_items = [
        {
            'name': 'Тест-полоски к анализатору мочи полуавтоматическому Н-500 DERUI(КНР)',
            'description': 'тест-полоски: DIRUI H11-МА (Microalbumin) №100 в наборе(руб).',
            'price': 1200,
        },
        {
            'name': 'Набор реагентов к Портативному флуоресцентному анализатору, предназначенному для измерения различных биомаркеров Wondfo(КНР)',
            'description': 'Набор реагентов для быстрого количественного определения сердечного тропонина I (cTn I), 25 шт/упак(руб).',
            'price': 15015,
        },
        {
            'name': 'Ковид-экспресс диагностика',
            'description': 'Экспресс-тест для опред. антигенов SARS-CoV-2 и вируса гриппа типов А и В, 25 шт/уп(руб).',
            'price': 3125,
        },
    ]
    context = {
        'pagename': 'Корзина',
        'content': 'Ваша корзина:',
        'cart_items': cart_items,
    }
    return render(request, 'fourth_task/basket.html', context)


def sign_up_by_django(request: HttpRequest):
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
            elif User.objects.filter(username=username).exists():  # Проверка в базе данных
                info["error"] = "Пользователь уже существует"
            else:
                # Создание нового пользователя
                User.objects.create(username=username, password=password, age=age)
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()

    info["form"] = form
    return render(request, "fourth_task/registration_page.html", info)


def sign_up_by_html(request: HttpRequest):
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
        elif User.objects.filter(username=username).exists():  # Проверка в базе данных
            info["error"] = "Пользователь уже существует"
        else:
            # Создание нового пользователя
            User.objects.create(username=username, password=password, age=int(age))
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, "fourth_task/registration_page.html", info)