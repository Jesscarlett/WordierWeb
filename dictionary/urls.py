from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dictionary', views.dict_view, name='dict_view'),
    path('pswords', views.junior_senior_words, name='pswords'),
    path('seniorwords', views.senior_words, name='seniorwords'),
    path('jokes_quotes', views.jokes_quotes, name='jokes_quotes'),
    path('quotes', views.quotes, name='quotes'),
    path('conversations', views.conversations, name='conversations'),
    path('choice_helper', views.choice_helper, name='choice_helper'),
    path('thesaurus', views.thesaurus, name='thesaurus'),
    path('fill_sentence', views.fill_sentence, name='fill_sentence'),
    path('paragraph', views.paragraph, name='paragraph'),
    path('hangman_junior', views.hangman_junior, name='hangman_junior'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy')
]

