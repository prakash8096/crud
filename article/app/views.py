from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Articles
from django.urls import reverse_lazy

# Create your views here.
class Data(ListView):
    model=Articles
    template_name='home.html'
class Detail(DetailView):
    model=Articles
    context_object_name ='batman'
    template_name='detail.html'
class Create(CreateView):
    model=Articles
    fields='__all__'
    template_name='new.html'
class Update(UpdateView):
    model=Articles
    fields=['title','text']
    template_name='edit.html'
class Delete(DeleteView):
    model=Articles
    template_name='delete.html'
    success_url = reverse_lazy('home')
    

