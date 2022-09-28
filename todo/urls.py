from django.urls import path
from . import views as todo_views

urlpatterns = [
    path("card-items/", todo_views.GetCardItemView.as_view(), name="card-items"),
    path("add-card/", todo_views.CreateCardView.as_view(), name="add-card"),
    path(
        "<int:card_id>/update-card/",
        todo_views.UpdateCardView.as_view(),
        name="update-card",
    ),
    path(
        "<int:card_id>/delete-card/",
        todo_views.DeleteCardView.as_view(),
        name="delete-card",
    ),
    # Todo API
    path("todo-items/", todo_views.TodoItemView.as_view(), name="todo-item"),
    path(
        "create-todo-item/", todo_views.CreateTodoItemView.as_view(), name="todo-item"
    ),
    path(
        "<int:todo_id>/delete-todo/",
        todo_views.DeleteTodoView.as_view(),
        name="delete-todo",
    ),
    path(
        "<int:todo_id>/update-todo/",
        todo_views.UpdateTodoView.as_view(),
        name="delete-todo",
    ),
    path(
        "<int:todo_id>/complete-todo/",
        todo_views.DoneTodoView.as_view(),
        name="complete-todo",
    ),
]
