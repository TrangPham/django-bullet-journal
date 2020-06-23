from django.shortcuts import render
from django.http import HttpResponse

from .models import List

def index(request):
    output = ""
    for l in List.objects.all():
        output += l.name
        output += "\n".join(l.view())
    return HttpResponse(output)
