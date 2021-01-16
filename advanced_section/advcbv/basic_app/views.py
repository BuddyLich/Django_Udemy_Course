from . import models
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse


class SchoolListView(ListView):
    model = models.School


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
