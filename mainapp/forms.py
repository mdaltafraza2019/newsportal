from django.forms import ModelForm
from .models import *

class newsform(ModelForm):
    class Meta:
        model=Post
        fields="__all__"