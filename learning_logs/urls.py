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
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
    # Adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Adding new entries
    path('new_entry/(<int:topic_id>)/', views.new_entry, name='new_entry'),
    # Editing entry
    path('edit_entry/(<int:entry_id>)', views.edit_entry, name='edit_entry')
]