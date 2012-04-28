from django import forms
from django.forms import ModelForm

from bootstrap.models import ExampleFields

class ExampleForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(),max_length=100) 
    password2 = forms.CharField(
        widget=forms.PasswordInput(),max_length=100)   
    class Meta:
        model = ExampleFields
        
class AjaxAutoComplete(forms.Form):
    name = forms.CharField(help_text="Enter a course name, e.g Psychology 100",
        label="Course Name",
        widget=forms.TextInput(attrs={'class':'xlarge'}))
        
class PopoverForm(forms.Form):
    popover_input = forms.CharField(label="Form Input Popover",
        widget=forms.TextInput(attrs={'class':'xlarge', 
            'data-content' : 'On focus, this appears - defined in forms.py',
            'data-original-title' : 'My title'}))