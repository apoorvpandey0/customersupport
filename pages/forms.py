from django import forms
from pages.models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title','selection_mode']
