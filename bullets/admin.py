from django.contrib import admin

from .models import *

admin.site.register(Bullet)
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Event)
admin.site.register(List)
admin.site.register(ListItem)