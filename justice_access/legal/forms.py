from django import forms
from .models import LegalAidRequest

#form to handel user input
class LegalAidRequestForm(forms.ModelForm):
    class Meta:
        model = LegalAidRequest
        fields = ['name', 'email', 'phone', 'issue_description']