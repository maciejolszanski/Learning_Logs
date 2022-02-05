from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

def index(request):
    '''Main website of learning_logs app'''

    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''Display the list of topics'''

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Display the list of each entry of the topic'''
    topic = get_object_or_404(Topic, id=topic_id)

    # Check whether the topic belong to this user
    _check_topic_owner(topic,request)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''Form to add a new Topic'''

    if request.method != 'POST':
        # If the request is not Post (it is GET) - create empty form
        form = TopicForm()
    else:
        # Data entered via POST method
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    
    # Display empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Add new entry to the topic'''

    topic = Topic.objects.get(id=topic_id)

    _check_topic_owner(topic,request)

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

@login_required
def edit_entry(request, entry_id):
    '''Edit exisiting entry'''

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    _check_topic_owner(topic,request)

    if request.method != 'POST':
        # If the method is not POST its probably GET
        form = EntryForm(instance=entry)
    else:
        # if the method is POST, update the entry
        form = EntryForm(instance=entry, data=request.POST)
        form.save()
        return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def _check_topic_owner(top,req):
    if top.owner != req.user:
        raise Http404
