from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('check_letter/', views.check_letter, name='check_letter'),
]
