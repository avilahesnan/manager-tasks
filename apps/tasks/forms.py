from django import forms
from apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        edit_mode = kwargs.pop('edit_mode', False)
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()

        if not edit_mode:
            self.fields.pop('is_completed')
        else:
            self.fields['is_completed'].widget.attrs['class'] = 'form-checkbox'

    class Meta:
        model = Task
        exclude = []
        labels = {
            'name': 'Name',
            'category': 'Category',
            'subject': 'Subject',
            'description': 'Description',
            'term': 'Term',
            'user': 'User',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input form-textarea'}),  # noqa : E501
            'term': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-input'
                }
            ),
            'user': forms.HiddenInput(),
        }
