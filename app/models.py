from django.contrib.auth.models import User
from django.db import models


class Advantage(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)  # Явно добавляем поле id
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_favorite = models.BooleanField(default=False)  # Поле для "избранного"
    description = models.TextField()
    likes_count = models.IntegerField(default=0)  # Количество лайков
    dislikes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Rating(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Advantage, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'achievement')


# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     achievement = models.ForeignKey(Advantage, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    advantage = models.ForeignKey(Advantage, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.advantage.name} by {self.name} on {self.created_at}'
