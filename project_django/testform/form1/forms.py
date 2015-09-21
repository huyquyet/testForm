from django import forms
from django.forms import Textarea
from form1.test.models import Information


class CreateForm(forms.ModelForm):
    email_confirm = forms.EmailField()

    class Meta:
        model = Information
        fields = ['first_name', 'last_name', 'email', 'email_confirm', 'birthday', 'address', 'description']
        widgets = {
            'first_name': Textarea(attrs={'cols': 50, 'rows': 1}),
            'last_name': Textarea(attrs={'cols': 50, 'rows': 1}),
            'address': Textarea(attrs={'cols': 50, 'rows': 2}),
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }

        def clean_email_confirm(self):
            email1 = self.cleaned_data.get('email')
            email_con = self.cleaned_data.get('email_confirm')
            if email1 != email_con:
                raise forms.ValidationError('Email ko trung khop')
            return email1


class EditForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['first_name', 'last_name', 'email', 'birthday', 'address', 'description']
        widgets = {
            'first_name': Textarea(attrs={'cols': 50, 'rows': 1}),
            'last_name': Textarea(attrs={'cols': 50, 'rows': 1}),
            'address': Textarea(attrs={'cols': 50, 'rows': 2}),
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
