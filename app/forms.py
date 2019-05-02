from django import forms
from .import models


class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['email','message']

class LocationForm(forms.ModelForm):
    class Meta:
        model = models.Location
        fields = ['location']