"""
URL configuration for sitewomen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from women.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    # через include ми достукуємося до всіх урлок в файлі /home/sawa/git/Good_Good_Django/Good_Django_Project/sitewomen/women/urls.py
    # path('women/' - ми показуємо який корневий url буде до "додатка" його можна і пустим зробити і буде вигляд що то основа
]


#це handler404 є вшите в джанго і тут просто його переоприділяємо
#https://docs.djangoproject.com/en/5.0/ref/urls/
handler404 = page_not_found