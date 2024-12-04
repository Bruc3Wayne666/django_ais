from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AchievementForm, ReviewForm
from .models import Advantage, Rating


def achievements(request):
    sort_by = request.GET.get('sort', 'created_at')  # По умолчанию сортировка по дате создания
    advantages = Advantage.objects.all().order_by(sort_by)
    return render(request, 'achievements.html', {'advantages': advantages})


def achievement(request, achievement_id):
    achievement_ = get_object_or_404(Advantage, id=achievement_id)

    reviews = achievement_.reviews.all()

    return render(request, 'achievement.html', {
        'achievement': achievement_,  # Передаем ачивку
        # 'form': form,  # Передаем форму для отзыва
        'reviews': reviews  # Передаем список отзывов
    })

    # return render(request, 'achievement.html', {'achievement': achievement_})


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


def rate_achievement(request, achievement_id):
    achievement = get_object_or_404(Advantage, id=achievement_id)
    rating, created = Rating.objects.get_or_create(user=request.user, achievement=achievement)
    rating.liked = not rating.liked  # Переключаем оценку
    rating.save()
    return redirect('achievements')  # Перенаправление на страницу достижений


def like_advantage(request, achievement_id):
    if request.method == 'POST':
        advantage = get_object_or_404(Advantage, id=achievement_id)
        advantage.likes_count += 1  # Увеличиваем количество лайков
        advantage.save()  # Сохраняем изменения
        return redirect('achievements')  # Перенаправляем обратно на страницу достижений


def dislike_advantage(request, achievement_id):
    if request.method == 'POST':
        advantage = get_object_or_404(Advantage, id=achievement_id)
        advantage.dislikes_count += 1  # Увеличиваем количество дизлайков
        advantage.save()  # Сохраняем изменения
        return redirect('achievements')  #


# def add_review(request, achievement_id):
#     achievement = get_object_or_404(Advantage, id=achievement_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.achievement = achievement
#             review.save()
#             return redirect('achievement', achievement_id=achievement.id)  # Перенаправление на страницу достижения
#     else:
#         form = ReviewForm()
#     return render(request, 'achievements/add_review.html', {'form': form, 'achievement': achievement})

def advantage_detail(request, achievement_id):
    # Получаем ачивку по ID или возвращаем 404, если не найдена
    advantage = get_object_or_404(Advantage, id=achievement_id)

    # Обработка POST-запроса для добавления нового отзыва
    if request.method == 'POST':
        print('00000000000000000000000000000')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  # Создаем объект отзыва, но не сохраняем его в БД
            review.advantage = advantage  # Привязываем отзыв к текущей ачивке
            review.save()  # Сохраняем отзыв в БД
            # return redirect('achievement', achievement=advantage)  # Перенаправляем на страницу ачивки

            # return redirect('achievement', achievement_id=advantage.id)  # Перенаправляем на страницу ачивки

            reviews = advantage.reviews.all()

            return render(request, 'achievement.html', {
                'achievement': advantage,  # Передаем ачивку
                'form': form,  # Передаем форму для отзыва
                'reviews': reviews  # Передаем список отзывов
            })

    else:
        print('---------------------------')
        form = ReviewForm()  # Если GET-запрос, создаем пустую форму

    # Получаем все отзывы, связанные с данной ачивкой
    reviews = advantage.reviews.all()

    print(reviews)
    # Отправляем данные в шаблон
    return render(request, 'achievement.html', {
        'achievement': advantage,  # Передаем ачивку
        'form': form,  # Передаем форму для отзыва
        'reviews': reviews  # Передаем список отзывов
    })
