
from django import forms
from .models import ContactModel, hackathonRegModel,InternshipModel,CompetetionModel, scholarshipModel, jobModel
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
            'team': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
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