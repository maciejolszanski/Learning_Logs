'''Defines urls patters for users app'''

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Default authentication URL
    path('', include('django.contrib.auth.urls')),
    # Register site
    path('register/', views.register, name='register')
]