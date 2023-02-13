from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dictionary', views.dict_view, name='dict_view'),
    path('pswords', views.junior_senior_words, name='pswords'),
    path('seniorwords', views.senior_words, name='seniorwords'),
    path('jokes_quotes', views.jokes_quotes, name='jokes_quotes')
]

