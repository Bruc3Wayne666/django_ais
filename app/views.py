from django.shortcuts import render, get_object_or_404, redirect

from .forms import AchievementForm
from .models import Advantage


def achievements(request):
    sort_by = request.GET.get('sort', 'created_at')  # По умолчанию сортировка по дате создания
    advantages = Advantage.objects.all().order_by(sort_by)
    return render(request, 'achievements.html', {'advantages': advantages})


def achievement(request, achievement_id):
    achievement_ = get_object_or_404(Advantage, id=achievement_id)
    return render(request, 'achievement.html', {'achievement': achievement_})


def achievement_create(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achievements')  # Замените на ваше URL для списка достижений
    else:
        form = AchievementForm()
    return render(request, 'achievement_form.html', {'form': form})


def achievement_update(request, achievement_id):
    achievement = get_object_or_404(Advantage, id=achievement_id)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect('achievement', achievement_id=achievement.id)  # Замените на ваше URL для деталей достижения
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'achievement_form.html', {'form': form})


def achievement_delete(request, achievement_id):
    achievement = get_object_or_404(Advantage, id=achievement_id)
    if request.method == 'POST':
        achievement.delete()
        return redirect('achievements')  # Замените на ваше URL для списка достижений
    return render(request, 'achievement_confirm_delete.html', {'achievement': achievement})
