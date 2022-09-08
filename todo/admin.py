from django.contrib import admin
from todo import models as todo_models

# Register your models here.
admin.site.register(todo_models.CardItem)
admin.site.register(todo_models.TaskItem)
