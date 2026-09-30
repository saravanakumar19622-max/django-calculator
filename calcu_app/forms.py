from django import forms
from .models import Calculation

class CalculationForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['num1', 'num2', 'operator']