from django.urls import path
from . import views as todo_views

urlpatterns = [path("todo-lists/", todo_views.TodoListView.as_view(), name="todo")]
