from django.forms import ModelForm
from django import forms
from .models import Contact, Pelatihan

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PelatihantForm(ModelForm):
    class Meta:
        model = Pelatihan
        fields = '__all__'
        widgets={
            'gender': forms.RadioSelect(
                attrs={
                    'class':'custom-control-input custom-control-label',
                }
            ),
        }