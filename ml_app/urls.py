# ml_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('predict/', views.predict, name='predict'),
]
