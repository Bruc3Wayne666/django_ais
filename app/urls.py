from django.urls import path
from .views import achievements

urlpatterns = [
    path('achievements/', achievements, name='achievements'),
]
