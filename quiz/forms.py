from django import forms
from .models import *


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['input_answer']
        # = forms.CharField(label='Answer ', widget=forms.Textarea)


# class RadioModelForm(forms.ModelForm):
#     def __init__(self, question, *args, **kwargs):
#         super(RadioModelForm, self).__init__(question, *args, **kwargs)  # populates the post
#         self.fields['answer_option'].queryset = Radio.objects.filter(question_id=question.id)
#
#     class Meta:
#         model = Radio
#         fields = ['answer_option']
#         widget = {
#             'answer_option': forms.RadioSelect
#         }


class ChoiceForm(forms.Form):
    choice = forms.CharField(widget=forms.RadioSelect)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['question_id'].queryset = Question.objects.none()

    # class Meta:
    #     model = Choice
    #     fields = ['text']
    #     widget = {
    #         'text': forms.CharField(label='Choice Option')
    #     }


