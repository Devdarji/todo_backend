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
]
