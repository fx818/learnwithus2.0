from django import forms
from .models import ContactModel
class contactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        labels = {
            'name':'Your name',
            'college':'College Name',
            'mobile': 'Phone Number',
            'email':'Email Address',
            'question':'Your question'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'college': forms.TextInput(attrs={'placeholder': 'Enter your college name'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'question': forms.TextInput(attrs={'placeholder': 'Enter your question'}),
        }

