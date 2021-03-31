from django import forms
from .models import *


class TextForm(forms.Form):
    input_answer = forms.CharField(label='Answer: ', widget=forms.Textarea)
