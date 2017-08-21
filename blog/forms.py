from django import forms

from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = (
        'title', 'description', 'created_date',
        'published_date', 'issue', 'wheelchair_accessible', 'money',
        'parentalconsent', 'min_age', 'max_age', 'transportation', 'contact',
        'insurance', 'hotline', 'self_health', 'therapy', 'games',
        'games', 'audio', 'affirmations', 'animals', 'c_visuals',
        'hobbies', 'meditate', 'spaces', 'vent', 'visuals',
        )
