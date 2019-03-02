from django import forms

class NameForm(forms.Form):
    user_name = forms.CharField(label = 'Your Name', max_length=100)