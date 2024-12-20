from django.shortcuts import render

def labtorg(request):
    context = {
        'pagename': 'Лабораторное оборудование',
        'content': 'Добро пожаловать на страницу лабораторного оборудования!',
    }
    return render(request, 'fourth_task/labtorg.html', context)

def reagents(request):
    items = {
        'item1': {
            'name': 'Тест-полоски к анализатору мочи полуавтоматическому Н-500 DERUI(КНР)',
            'description': 'тест-полоски: DIRUI H11-МА (Microalbumin) №100 в наборе(руб).',
            'price': 1200,
        },
        'item2': {
            'name': 'Набор реагентов к Портативному флуоресцентному анализатору, предназначенному для измерения различных биомаркеров Wondfo(КНР)',
            'description': 'Набор реагентов для быстрого количественного определения сердечного тропонина I (cTn I), 25 шт/упак(руб).',
            'price': 15015,
        },
        'item3': {
            'name': 'Ковид-экспресс диагностика',
            'description': 'Экспресс-тест для опред. антигенов SARS-CoV-2 и вируса гриппа типов А и В, 25 шт/уп(руб).',
            'price': 3125,
        },
    }
    context = {
        'pagename': 'Реагенты',
        'content': 'Здесь вы можете найти наши реагенты.',
        'items': items,
    }
    return render(request, 'fourth_task/reagents.html', context)

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