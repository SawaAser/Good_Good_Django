from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = ['Про сайт', 'Додати статтю', 'Зворотній звязок', 'Зайти']


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
    {'id': 1, 'title': 'Анджеліна Джолі', 'content': 'Біографія Анджеліни Джолі', 'id_published': True},
    {'id': 2, 'title': 'Марго Роббі', 'content': 'Біографія Марго Роббі', 'id_published': False},
    {'id': 3, 'title': 'Джулі Робертс', 'content': 'Біографія Джулі Робертс', 'id_published': True},
]


def index(request): # HTTPrequest
    data = {'title': 'Головна сторінка',
            'menu': menu,
            'posts': data_db
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'Про сайт'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статті по категоріях</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статті по категоріях</h1><p>cat_slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        # return redirect(uri)  # найкращий варіант
        # return HttpResponseRedirect(uri)
        return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f'<h1>Архів по роках</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка незнайдена</h1>")