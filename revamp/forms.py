from django.forms import ModelForm
from .models import Contact, pelatihan


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class pelatihantForm(ModelForm):
    class Meta:
        model = pelatihan
        fields = '__all__'