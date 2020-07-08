from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ValidationError
from django.views import generic

from bullets.models import *

class DetailView(generic.DetailView):
    template_name = 'bullets/detail.html'
    context_object_name = 'object'

class NoteView(DetailView):
    model = Note

def task(request, uuid):
    return handle_get(Task, uuid)

def note(request, uuid):
    return handle_get(Note, uuid)

def event(request, uuid):
    return handle_get(Event, uuid)

def handle_get(model, uuid):
    try:
        obj = model.objects.get(uuid=uuid)
    except ValidationError:
        return HttpResponse(status=400)
    except model.DoesNotExist:
        raise Http404("Task does not exist.")

    return HttpResponse(str(obj))    
