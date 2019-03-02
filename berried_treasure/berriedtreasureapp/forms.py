from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label = 'Your Name', max_length=12)
    comment = forms.CharField(label = 'Your Comment', max_length=280, widget=forms.Textarea)