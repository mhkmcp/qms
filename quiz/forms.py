from django import forms
from .models import *


class TextForm(forms.Form):
    input_answer = forms.CharField(label='Answer ', widget=forms.Textarea)


class RadioModelForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(RadioModelForm, self).__init__(*args, **kwargs)  # populates the post
        # self.fields['answer_option'].queryset = Choice.objects.fil

    class Meta:
        model = Radio
        fields = ['answer_option']
        widget = {
            'answer_option': forms.RadioSelect
        }


# class TextForm(forms.Form):
#     input_answer = forms.Textarea()

