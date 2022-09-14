from django.contrib import admin
from todo import models as todo_models


# Register your models here.
@admin.register(todo_models.CardItem)
class CardItemAdmin(admin.ModelAdmin):
    list_display = ["card_name", "created_date_time", "updated_date_time", "is_active"]


@admin.register(todo_models.TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_date_time",
        "updated_date_time",
        "is_pending",
        "is_active",
    ]
