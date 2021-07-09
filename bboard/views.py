from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.dates import ArchiveIndexView
from django.template import loader
from django.shortcuts import render
from .forms import BbForm
from django.urls import reverse_lazy, reverse

from .models import Bb, Rubric

def index(request):
    #template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    #context = { 'bbs' : bbs}
    #return HttpResponse(template.render(context, request))
    return render(request,'bboard/index.html', context)
   

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs , 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render (request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/bboard/detail/{id}'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbDeleteView(DeleteView):
    model = Bb
    success_url = reverse_lazy('index')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbAddView(FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object
    def get_success_url(self):
        return reverse('by_rubric', kwargs={'rubric_id':self.object.cleaned_data['rubric'].pk})

class BbDetailView(DetailView):
    model = Bb
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbByRubricView(ListView):
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'
    def get_queryset(self):
        return Bb.objects.filter(rubric = self.kwargs['rubric_id'])
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context
        
class BbIndexView(ArchiveIndexView):
    model = Bb
    date_field = 'published'
    template_name = 'bboard/index.html'
    context_object_name = 'bbs'
    allow_empty = True
    def get__context_data (self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

 


""" def add_and_save (request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric',kwargs={ 'rubric_id':bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)
    else:
        bbf = BbForm ()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context) """



   

""" def add(request):
    bbf = BbForm ()
    context = {'form': bbf}
    return render (request, 'bboard/create.html', context)

def add_save(request):
    bbf = BbForm(request.POST)
    if bbf.is_valid():
        bbf.save ()
        return HttpResponseRedirect (reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk} ))
    else:
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context) """
    
 