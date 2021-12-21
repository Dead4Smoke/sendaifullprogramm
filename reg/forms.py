from django.contrib.auth.models import User
from django import forms
from django import forms

class Loginsform(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}), required=True) 
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Введите логин', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    