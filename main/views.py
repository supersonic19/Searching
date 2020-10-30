from django.shortcuts import render
from main import models
from main import forms
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView
)
from django.db.models import Q
from django.views.generic.edit import FormView
# Create your views here.

class search(TemplateView):
    template_name = 'search.html'

class result_view(ListView):

    template_name = 'results.html'
    model = models.Expert

    def get_queryset(self):

        query = self.request.GET.get('q')
        object_list = models.Expert.objects.filter(
            field = query
        )

        return object_list



