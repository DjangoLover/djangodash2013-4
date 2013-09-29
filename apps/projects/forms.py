from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Project, Card


class ProjectCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Project
        exclude = ('slug', 'owner', 'deleted')


class CardCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Card
        exclude = ('slug', 'content', 'project', 'deleted', 'done')
