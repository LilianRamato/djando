from django import  forms
from djangoafternoonn.model import  Students
class EmpForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"