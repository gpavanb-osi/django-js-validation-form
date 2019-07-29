from django.urls import path

from . import views

urlpatterns = [
    path('home', views.IndexView),
    path('registration', views.Registration)
]