from django.shortcuts import render
from .models import Advantage

def achievements(request):
    sort_by = request.GET.get('sort', 'created_at')  # По умолчанию сортировка по дате создания
    advantages = Advantage.objects.all().order_by(sort_by)
    return render(request, 'achievements.html', {'advantages': advantages})
