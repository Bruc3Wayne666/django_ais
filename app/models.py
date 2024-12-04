from django.db import models


class Advantage(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_favorite = models.BooleanField(default=False)  # Поле для "избранного"

    def __str__(self):
        return self.title
