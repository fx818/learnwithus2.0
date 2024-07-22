from django import forms
from .models import hackathonRegModel

class hackathonRegForm(forms.ModelForm):
    class Meta:
        model = hackathonRegModel
        fields = '__all__'
        # team,college,lead,leadmobile,leadmail,mem2,m2mobile,mem3,m3mobile,year,branch
        labels = {
            'team':'Team name',
            'college':'College Name',
            'lead': 'Lead name',
            'leadmobile':'Lead Mobile',
            'leadmail':'Lead Mail',
            'mem2':'Member 2',
            'm2mobile':'Mobile',
            'mem3':'Member 3',
            'm3mobile':'Mobile',
            'year':'Year',
            'branch':'Branch',
        }
        widgets = {
            'team': forms.TextInput(attrs={'placeholder': f"Enter your name"}),
            'college': forms.TextInput(attrs={'placeholder': 'Enter your college name'}),
            'lead': forms.TextInput(attrs={'placeholder': 'Enter your lead name'}),
            'leadmobile': forms.TextInput(attrs={'placeholder': 'Enter lead\'s mobile'}),
            'leadmail': forms.EmailInput(attrs={'placeholder': 'Enter lead\'s mail'}),
            'mem2': forms.TextInput(attrs={'placeholder': 'Enter member 2'}),
            'm2mobile': forms.TextInput(attrs={'placeholder': 'Enter member 2 mobile'}),
            'mem3': forms.TextInput(attrs={'placeholder': 'Enter member 3'}),
            'm3mobile': forms.TextInput(attrs={'placeholder': 'Enter member 3 mobile'}),
            'year': forms.TextInput(attrs={'placeholder': 'Enter your year'}),
            'branch': forms.TextInput(attrs={'placeholder': 'Enter your branch'}),
        }
