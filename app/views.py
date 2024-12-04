from django.shortcuts import render, get_object_or_404
from .models import Advantage


def achievements(request):
    sort_by = request.GET.get('sort', 'created_at')  # По умолчанию сортировка по дате создания
    advantages = Advantage.objects.all().order_by(sort_by)
    return render(request, 'achievements.html', {'advantages': advantages})


def achievement(request, achievement_id):
    achievement_ = get_object_or_404(Advantage, id=achievement_id)
    return render(request, 'achievement.html', {'achievement': achievement_})
