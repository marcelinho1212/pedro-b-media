from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["full_name", "email", "service", "message"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email"
                }
            ),
            "service": forms.TextInput(
                attrs={
                    "placeholder": "Example: Basic package, custom video, editing"
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell us more about your project",
                    "rows": 6
                }
            ),
        }