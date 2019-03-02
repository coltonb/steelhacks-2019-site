from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import NameForm
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class ResultsPageView(TemplateView):
    template_name = "results.html"

def get_name(request):
    if(request.method == 'POST'):
        form = NameForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('/results/')
    else:
        form = NameForm()
    
return render(request, 'index.html', {'form': form})
    