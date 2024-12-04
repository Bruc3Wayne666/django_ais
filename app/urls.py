from django.urls import path
from .views import achievements, achievement

urlpatterns = [
    path('achievements/', achievements, name='achievements'),
    path('achievement/<int:achievement_id>/', achievement, name='achievement'),
]
