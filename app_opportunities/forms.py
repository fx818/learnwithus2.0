from django import forms
from .models import InternshipModel,CompetetionModel, scholarshipModel, jobModel



class internshupUpdateForm(forms.ModelForm):
    class Meta:
        model = InternshipModel
        fields = '__all__'
        labels = {
            'title': 'Title',
            'link': 'References',
            'image': 'Picture',
            'desc': 'Short description'
        }
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Enter the title'}),
            'link':forms.TextInput(attrs={'placeholder':'Place the link here'}),
            'desc':forms.TextInput(attrs={'placeholder':'Please write the description'}),
        }

class competetionUpdateForm(forms.ModelForm):
    class Meta:
        model = CompetetionModel
        fields = '__all__'
        labels = {
            'title': 'Title',
            'link': 'References',
            'image': 'Picture',
            'desc': 'Short description'
        }
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Enter the title'}),
            'link':forms.TextInput(attrs={'placeholder':'Place the link here'}),
            'desc':forms.TextInput(attrs={'placeholder':'Please write the description'}),
        }

class scholarshipUpdateForm(forms.ModelForm):
    class Meta:
        model = scholarshipModel
        fields = '__all__'
        labels = {
            'title': 'Title',
            'link': 'References',
            'image': 'Picture',
            'desc': 'Short description'
        }
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Enter the title'}),
            'link':forms.TextInput(attrs={'placeholder':'Place the link here'}),
            'desc':forms.TextInput(attrs={'placeholder':'Please write the description'}),
        }

class jobUpdateForm(forms.ModelForm):
    class Meta:
        model = jobModel
        fields = '__all__'
        labels = {
            'title': 'Title',
            'link': 'References',
            'image': 'Picture',
            'desc': 'Short description'
        }
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Enter the title'}),
            'link':forms.TextInput(attrs={'placeholder':'Place the link here'}),
            'desc':forms.TextInput(attrs={'placeholder':'Please write the description'}),
        }