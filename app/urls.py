from django.urls import path
from .views import achievements, achievement, achievement_create, achievement_update, achievement_delete, like_advantage, dislike_advantage, advantage_detail

urlpatterns = [
    path('achievements/', achievements, name='achievements'),
    path('achievement/<int:achievement_id>/', achievement, name='achievement'),

    path('achievement/add/', achievement_create, name='achievement_create'),
    path('achievement/<int:achievement_id>/edit/', achievement_update, name='achievement_update'),
    path('achievement/<int:achievement_id>/delete/', achievement_delete, name='achievement_delete'),

    path('like_achievement/<int:achievement_id>/', like_advantage, name='like_achievement'),
    path('dislike_achievement/<int:achievement_id>/', dislike_advantage, name='dislike_achievement'),

    path('review/<int:achievement_id>/', advantage_detail, name='review'),

]

