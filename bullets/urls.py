from django.urls import path

from . import views

app_name = "bullets"
urlpatterns = [
    path("notes/", views.NoteIndexView.as_view(), name="note-index"),
    path("tasks/", views.TaskIndexView.as_view(), name="task-index"),
    path("events/", views.EventIndexView.as_view(), name="event-indexx"),
    path("notes/add/", views.note_add, name="note-add"),
    path("tasks/add/", views.task_add, name="task-add"),
    path("events/add/", views.event_add, name="event-add"),
    path("notes/<str:pk>/", views.NoteDetailView.as_view(), name="note-detail"),
    path("tasks/<str:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("events/<str:pk>/", views.EventDetailView.as_view(), name="event_detail"),
]
