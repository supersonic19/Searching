'''from django import forms
from django.views.generic.edit import FormView
from main import models


class info_form(forms.ModelForm):

    class Meta:
        model = models.info
        fields = '__all__'

        widgets = {
            'password' : forms.PasswordInput,
            'phone'  : forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter numbers Only '})
        }'''