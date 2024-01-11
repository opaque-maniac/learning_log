from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.http import Http404
from .models import Topic, Entry
from .forms import EntryForm, TopicForm

# View for the landing page
def landing(request):
    if request.user.is_authenticated:
        return redirect(reverse('learning_log:home'))
    return render(request, 'learning_log/landing.html')

# View for the home page
@login_required
def home(request):
    topics = Topic.objects.filter(author=request.user)
    return render(request, 'learning_log/home.html', {
        'topics': topics
    })

# View for the new topic page
@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect(reverse('learning_log:individual_topic', args=[str(topic.id)]))
    else:
        form = TopicForm()
    return render(request, 'learning_log/new_topic.html', {
        'form': form
    })

# View for individual topic page
@login_required
def individual_topic(request, topic_id):
    this_topic = Topic.objects.get(id=topic_id)
    if this_topic.author != request.user:
        raise Http404(_("Persmission denied"))
    entries = Entry.objects.filter(topic=this_topic)
    return render(request, 'learning_log/individual_topic.html', {
        'topic': this_topic,
        'entries': entries
    })

# View for the delete topic page
@login_required
def delete_topic(request, topic_id):
    this_topic = Topic.objects.get(id=topic_id)
    if this_topic.author != request.user:
        raise Http404(_("Permission denied"))
    if request.method == 'POST':
        this_topic.delete()
        return redirect(reverse('learning_log:home'))
    else:
        return render(request, 'learning_log/delete_topic.html', {
            'topic': this_topic
        })

# View for the new entry page
@login_required
def new_entry(request, topic_id):
    this_topic = Topic.objects.get(id=topic_id)
    if this_topic.author != request.user:
        raise Http404(_("Permission denied"))
    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = this_topic
            entry.save()
            return redirect(reverse('learning_log:individual_topic', args=[str(this_topic.id)]))
    else:
        form = EntryForm()
    return render(request, 'learning_log/new_entry.html', {
        'form': form,
        'topic': this_topic
    })

# View for the individual entry page
@login_required
def individual_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.topic.author != request.user:
        raise Http404(_("Permission denied"))
    return render(request, 'learning_log/individual_entry.html', {
        'entry': entry
    })

# View for the edit entry page
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.topic.author != request.user:
        raise Http404(_("Permission denied"))
    if request.method == 'POST':
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('learning_log:individual_entry', args=[str(entry.id)]))
    else:
        form = EntryForm(instance=entry)
    return render(request, 'learning_log/edit_entry.html', {
        'form': form,
        'topic': entry.topic,
        'entry_id': entry.id
    })

# View for the delete entry page
@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.topic.author != request.user:
        raise Http404(_("Permission denied"))
    if request.method == 'POST':
        entry.delete()
        return redirect(reverse('learning_log:individual_topic', args=[str(entry.topic.id)]))
    else:
        return render(request, 'learning_log/delete_entry.html', {
            'topic': entry.topic,
            'entry': entry,
            'entry_text': entry.text[:50]
        })
