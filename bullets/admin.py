from django.contrib import admin

from .models import *

admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Event)