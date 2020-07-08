from django.urls import path

from . import views

urlpatterns = [
    path('notes/<str:pk>/', views.NoteView.as_view() , name='note'),
    path('tasks/<str:uuid>/', views.task, name='task'),
    path('events/<str:uuid>/', views.event, name='event'),
]