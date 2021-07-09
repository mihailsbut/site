from django import forms
from .models import Bb


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ('title','content','price','rubric')