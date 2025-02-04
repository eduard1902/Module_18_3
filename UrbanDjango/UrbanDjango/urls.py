"""
URL configuration for UrbanDjango project.

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
from django.urls import path
from task2.views import home_view
from django.views.generic import  TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('class/', TemplateView.as_view(template_name='func_template.html')),
    path('platform/', TemplateView.as_view(
        template_name='platform.html',
        extra_context={'message': 'Главная страница',
                       'title': 'Главная',
                       'games': 'Магазин',
                       'cart': 'Корзина'
                       })),
    path('platform/games/', TemplateView.as_view(
        template_name='games.html',
        extra_context={'game': 'Игры',
                       'buy': 'Купить',
                       'game1': 'Atomik Heart',
                       'game2': 'Cyberpunk 2077',
                       'game3': 'PayDay'
                       }
    )),
    path('platform/cart', TemplateView.as_view(
        template_name='cart.html',
        extra_context={'title': 'Корзина',
                       'message': 'Извините, ваша корзина пуста',

                       }
    )),
]
