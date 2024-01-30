from django import forms
from apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_completed', 'user']
        labels = {
            'name': 'Name',
            'category': 'Category',
            'subject': 'Subject',
            'description': 'Description',
            'term': 'Term',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input form-textarea'}),
            'term': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-input'
                }
            ),
        }
