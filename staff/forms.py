from django import forms
from quiz.models import *


ANS_TYPE = (
    ('radio', 'Radio'),
    ('text', 'Text')
)


class QuestionModelForm(forms.ModelForm):
    # title = forms.CharField(label='Question Title: ', max_length=255)
    # answer_type = forms.ChoiceField(label='Answer Type: ',
    #                                 choices=ANS_TYPE,
    #                                 widget=forms.RadioSelect)
    class Meta:
        model = Question
        fields = ['title', 'answer_type']


class TextModelForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['correct_answer']


class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']


class MultipleChoiceForm(forms.Form):
    number = forms.IntegerField(label='Number of Choices ', min_value=2, max_value=8)
