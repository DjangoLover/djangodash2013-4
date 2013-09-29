from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Project
