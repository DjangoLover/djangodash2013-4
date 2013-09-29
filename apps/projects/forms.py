from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Project, Card, Board, ProjectComment, CardComment


class ProjectCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Project
        exclude = ('slug', 'owner', 'deleted')


class ProjectUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Project
        exclude = ('slug', 'owner')


class BoardCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoardCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Board
        exclude = ('project', 'position')



class CardCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Card
        exclude = ('slug', 'content', 'project', 'deleted', 'done')


class ProjectCommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCommentCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = ProjectComment
        exclude = ('author', 'project', 'content')


class CardCommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardCommentCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = CardComment
        exclude = ('author', 'project', 'card', 'content')