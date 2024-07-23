from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDifitYearConverter, "year4")

# urlpatterns = [
#     path('', views.index, name='home'),  # http://127.0.0.1:8000/women/
#     path('cats/<int:cat_id>/', views.categories, name='cats_id'),  # http://127.0.0.1:8000/women/cats/2/
#     path('about/', views.about, name='about'),
#
#     # тут важлива послідовність  бо slug збирає і числа і якщо б він був вище то до інта не доходилоб нічого
#     path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # http://127.0.0.1:8000/women/cats/sadfasd/
#
#     # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive), # заміняємо
#     path("archive/<year4:year>/", views.archive, name='archive'),
#     path('post/<int:post_id>/', views.show_post, name='post'),
# ]


urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/women/
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
