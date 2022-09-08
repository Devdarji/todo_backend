from django.db import models


# Create your models here.
class CardItem(models.Model):
    card_name = models.CharField(max_length=500, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)


class TaskItem(models.Model):
    card = models.ForeignKey(
        CardItem, on_delete=models.CASCADE, related_name="card_item"
    )
    title = models.CharField(max_length=1000, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField()
    is_pending = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)