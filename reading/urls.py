from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('alice_one', views.alice_one, name='alice_one'),
    ]