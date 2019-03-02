from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Entry
from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, 'index.html', { 'form': NameForm })

def results(request):
    if request.method == 'POST' :
        form = NameForm(request.POST)
        if form.is_valid():
            new_entry = Entry(name=form.cleaned_data['name'], comment=form.cleaned_data['comment'])
            new_entry.save()
            return HttpResponseRedirect('/results')
    else:
        return render(request, 'results.html', { 'entries' : Entry.objects.all().order_by("-date")[:10] })