# app/forms.py
from django import forms
from .models import Advantage, Review


# title
# created_at
# is_favorite
# description


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Advantage
        fields = ['title', 'description', 'is_favorite']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
