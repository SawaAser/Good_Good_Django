from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


# menu = ['Про сайт', 'Додати статтю', 'Зворотній звязок', 'Зайти']

menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Добавити статю", 'url_name': 'add_page'},
        {'title': "Зворотній звязок", 'url_name': 'contact'},
        {'title': "Зайти", 'url_name': 'login'},
    ]


# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# def index(request): # HTTPrequest
#     # t = render_to_string('women/index.html')
#     # return HttpResponse(t)
#     data = {'title': 'Головна сторінка',
#             'menu': menu,
#             'float': 29.4,
#             'lst': [1, 2, 'abd', True],
#             'set': {1, 2, 3, 2, 5},
#             'dict': {'key1': 'value1', 'key2': 'value2'},
#             'obj': MyClass(10, 20),
#             'url': slugify("The Main Page")
#             }
#     return render(request, 'women/index.html', context=data)


data_db = [
    {'id': 1, 'title': 'Анджеліна Джолі', 'content': """<h1>Анджеліна Джолі</h1>(англ. Angelina Jolie, МФА: [dʒoʊˈliː]; Анджеліна Джолі Войт (англ. Angelina Jolie Voight); нар. 4 червня 1975, Лос-Анджелес) — американська акторка, фотомодель, режисерка, амбасадорка доброї волі ЮНІСЕФ, володарка двох премій «Оскар» (2000, 2014), трьох премій «Золотий глобус» (1998, 1999, 2000).
    
Дебютувала в кіно 1982 року, зігравши у фільмі «У пошуках виходу». Однак стала відомою після ролі Лари Крофт у фільмах «Лара Крофт: Розкрадачка гробниць» (2001) та «Лара Крофт розкрадачка гробниць: колиска життя» (2003). Серед інших відомих робіт — «Містер і місіс Сміт» (2005), «Особливо небезпечний» (2008) та «Солт» (2010). Вона також зобразила одну з вічних — воїнесу Тену у фільмі Кіносесвіту Marvel «Вічні» (2021).""",
     'id_published': True},
    {'id': 2, 'title': 'Марго Роббі', 'content': 'Біографія Марго Роббі', 'id_published': False},
    {'id': 3, 'title': 'Джулі Робертс', 'content': 'Біографія Джулі Робертс', 'id_published': True},
]


cats_db = [
    {'id': 1, 'name': 'Акторки'},
    {'id': 2, 'name': 'Співачки'},
    {'id': 3, 'name': 'Спортцменки'},
]


def index(request): # HTTPrequest
    data = {'title': 'Головна сторінка',
            'menu': menu,
            'posts': data_db,
            'car_selected': 0,
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'Про сайт', 'menu': menu})

# #__________________________________________
# # ЗАЙВЕ
#
#
# def categories(request, cat_id):
#     return HttpResponse(f'<h1>Статті по категоріях</h1><p>id: {cat_id}</p>')
#
#
# def categories_by_slug(request, cat_slug):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>Статті по категоріях</h1><p>cat_slug: {cat_slug}</p>')
#
#
# def archive(request, year):
#     if year > 2023:
#         uri = reverse('cats', args=('music', ))
#         # return redirect(uri)  # найкращий варіант
#         # return HttpResponseRedirect(uri)
#         return HttpResponsePermanentRedirect(uri)
#
#     return HttpResponse(f'<h1>Архів по роках</h1><p>{year}</p>')
#
#
# #__________________________________________


def show_post(request, post_id):
    return HttpResponse(f"Відображення статті з id = {post_id}")


def addpage(request):
    return HttpResponse("Додавання статті")


def contact(request):
    return HttpResponse("Зворотній звязок")


def login(request):
    return HttpResponse("Авторизація")


def show_category(request, cat_id):
    data = {'title': 'Відображення по категоріях',
            'menu': menu,
            'posts': data_db,
            'cat_selected': cat_id,
            }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка незнайдена</h1>")

