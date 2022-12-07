from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Series


class SeriesListView(ListView):
    template_name ="series/series_list.html"
    model = Series


class SeriesDetailView(DetailView):
    template_name ="series/series_detail.html"
    model = Series


class SeriesCreateView(CreateView):
    template_name ="series/series_create.html"
    model = Series
    fields = ["name","author","desc"]


class SeriesUpdateView(UpdateView):
    template_name ="series/series_update.html"
    model = Series
    fields = ["name","author","desc"]


class SeriesDeleteView(DeleteView):
    template_name ="series/series_delete.html"
    model = Series
    success_url = reverse_lazy("series_list")