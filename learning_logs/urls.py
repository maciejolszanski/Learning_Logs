'''define URL patterns for leraning_logs app'''

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Main site
    path('', views.index, name='index'),
    # Topics list site
    path('topics/', views.topics, name='topics'),
    # Site of each topic entries
    path('topics/(<int:topic_id>)/', views.topic, name='topic')
]