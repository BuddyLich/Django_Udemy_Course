from . import models
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = models.School
    # gets a school_list from above as default, you can also:
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
