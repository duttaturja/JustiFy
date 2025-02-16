from django.urls import path
from . import views

app_name = 'crime'

urlpatterns = [
    path('landing', views.index, name='index'),
]