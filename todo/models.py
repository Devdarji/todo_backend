from django.db import models


# Create your models here.
class CardItem(models.Model):
    card_name = models.CharField(max_length=500, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def get_card_details(self):
        task_instances = self.card_item.filter(is_active=True).last()
        if task_instances:
            return {
                "card_name": self.card_name,
                "title": task_instances.title if task_instances.title else "NA",
                "created_date_time": self.created_date_time,
                "updated_date_time": self.updated_date_time,
            }


class TaskItem(models.Model):
    card = models.ForeignKey(
        CardItem,
        on_delete=models.CASCADE,
        related_name="card_item",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=1000, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(null=True, blank=True)
    is_pending = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def get_task_details(self):
        return {
            "card": self.card.card_name if self.card else "NA",
            "title": self.title,
            "created_date_time": self.created_date_time,
            "updated_date_time": self.updated_date_time,
            "is_pending": self.is_pending,
        }
