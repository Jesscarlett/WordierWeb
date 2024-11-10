from django.urls import path
from .views import GenerateResponseView

urlpatterns = [
    path('api/gai/', GenerateResponseView.as_view(), name='gai_api'),
]