from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ValidationError
from django.views import generic

from bullets.models import Task, Note, Event


class IndexView(generic.ListView):
    template_name = "bullets/index.html"
    context_object_name = "list"

    def get_queryset(self):
        return self.model.objects.order_by("-created_at")[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["path"] = "bullets:{}-detail".format(self.model.__name__.lower())
        context["heading"] = self.model.__name__ + "s"
        return context


class NoteIndexView(IndexView):
    model = Note


class TaskIndexView(IndexView):
    model = Task


class EventIndexView(IndexView):
    model = Event


class DetailView(generic.DetailView):
    template_name = "bullets/detail.html"
    context_object_name = "object"


class NoteDetailView(DetailView):
    model = Note


class TaskDetailView(DetailView):
    model = Task


class EventDetailView(DetailView):
    model = Event
