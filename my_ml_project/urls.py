from django.contrib import admin
from django.urls import path
from ml_app import views  # Import your views from ml_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.predict, name='home'),  # Set the root URL to the predict view
    path('ml/predict/', views.predict, name='predict'),  # Original predict URL
]
