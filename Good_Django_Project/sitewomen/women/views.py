from django.http import HttpResponse
from django.shortcuts import render


def index(request): # HTTPrequest
    return HttpResponse('Сторінка додатку women')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статті по категоріях</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статті по категоріях</h1><p>cat_slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архів по роках</h1><p>{year}</p>')
