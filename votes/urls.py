from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learn', views.learn, name='learn'),
    path('remember', views.remember, name='remember'),
    path('about', views.about, name='about'),
    path('send', views.send, name='send'),
]
