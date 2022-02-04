from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    '''Form to add a new Topic'''

    if request.method != 'POST':
        # If the request is not Post (it is GET) - create empty form
        form = TopicForm()
    else:
        # Data entered via POST method
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    # Display empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    '''Add new entry to the topic'''

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Request is probably GET- so create an empty form
        form = EntryForm()
    else:
        # Request is POST - save the entry
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)

    # Dispaly the empty form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
