from django import forms
from .models import ContactModal

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModal
        fields = '__all__'