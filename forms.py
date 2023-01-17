from django import forms

from .models import usersignin
class user(forms.ModelForm):
    #name=forms.CharField(label="name",max_length=20)
    class Meta:
        model=usersignin
        fields="__all__" 