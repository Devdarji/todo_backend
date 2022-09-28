from django.db import models


# Create your models here.


class TaskItem(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(null=True, blank=True)
    is_pending = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def get_task_details(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_date_time": self.created_date_time,
            "updated_date_time": self.updated_date_time,
            "is_pending": self.is_pending,
        }

    class Meta:
        ordering = ("-id",)


class CardItem(models.Model):
    card_name = models.CharField(max_length=500, null=True, blank=True)
    task = models.ManyToManyField(TaskItem, related_name="task", null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def get_card_details(self):
        return {
            "id": self.id,
            "card_name": self.card_name,
            "title": [
                {"title": item.title, "is_pending": item.is_pending}
                for item in self.task.filter(is_active=True)
            ]
            if self.task
            else "NA",
            "created_date_time": self.created_date_time,
            "updated_date_time": self.updated_date_time,
        }
