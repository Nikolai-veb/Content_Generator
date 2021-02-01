from django import forms
from .models import Sites, Articles

class AddSitesForm(forms.ModelForm):
    """Add Sites"""
    class Meta:
        model = Sites
        fields = ("under_category", "url")