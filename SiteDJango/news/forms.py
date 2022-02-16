from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя кадра'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кликуха'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'гг-дд-мм часы:минуты:секунды'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Характеристика'
            })
        }