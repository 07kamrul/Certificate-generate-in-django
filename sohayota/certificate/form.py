from django.forms import ModelForm

from .models import *

class SohayotaForm(ModelForm):
    class Meta:
        model = Sohayota
        # fields = '__all__'
        fields = ['name', 'mobile_no', 'email_id', 'address', 'occupation']

