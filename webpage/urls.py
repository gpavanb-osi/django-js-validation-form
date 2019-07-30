from django.urls import path

from . import views

urlpatterns = [
    path('home', views.IndexView),
    path('regview', views.Registration)
]