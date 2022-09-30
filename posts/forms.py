from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['place','address','rent','bedroom','bathroom','size','phone','image']
