from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDifitYearConverter, "year4")

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000/women/
    path('cats/<int:cat_id>/', views.categories),  # http://127.0.0.1:8000/women/cats/2/
    # тут важлива послідовність  бо slug збирає і числа і якщо б він був вище то до інта не доходилоб нічого
    path('cats/<slug:cat_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/women/cats/sadfasd/
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive), # заміняємо
    path("archive/<year4:year>/", views.archive),
]

