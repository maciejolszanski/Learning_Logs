from django.shortcuts import render
from .models import Topic


def index(request):
    '''Main website of learning_logs app'''

    return render(request, 'learning_logs/index.html')

def topics(request):
    '''Display the list of topics'''

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''Display the list of each entry of the topic'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)
