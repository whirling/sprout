from django import forms

from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = (
        'title', 'description','games', 'audio', 'affirmations', 'animals', 'c_visuals',
        'hobbies', 'meditate', 'spaces', 'vent', 'visuals', 'hotline', 'self_help', 'therapy',
        'chat',
        )
