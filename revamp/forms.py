from django.forms import ModelForm
from .models import Contact, Pelatihan
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PelatihantForm(ModelForm):
    class Meta:
        model = Pelatihan
        fields = '__all__'
        widgets={
            'yesorno': forms.RadioSelect(
                attrs={
                    'class':'custom-control-input custom-control-label',
                }
            ),
        }