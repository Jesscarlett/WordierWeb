from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('alice_one', views.alice_one, name='alice_one'),
    path('alice_two', views.alice_two, name='alice_two'),
    path('alice_three', views.alice_three, name='alice_three'),
    path('alice_four', views.alice_four, name='alice_four'),
    ]