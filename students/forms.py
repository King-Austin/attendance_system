from django import forms

class LoginForm(forms.Form):
    regnumber = forms.CharField(max_length=10, min_length=10, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember = forms.CheckboxInput()