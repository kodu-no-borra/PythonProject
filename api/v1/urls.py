from django.urls import path
from .task import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),

    path('tasks/<int:pk>/', views.TaskRetrieveView.as_view(), name='task-retrieve'),

    path('tasks/<int:pk>/status/', views.TaskStatusUpdateView.as_view(), name='task-update-status'),

    path('tasks/<int:pk>/delete/', views.TaskDestroyView.as_view(), name='task-destroy'),
]