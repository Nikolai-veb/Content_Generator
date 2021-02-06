from django import forms
from .models import Sites, Articles

class AddArticlesForm(forms.ModelForm):
    """Add Sites"""
    class Meta:
        model = Sites
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
        }