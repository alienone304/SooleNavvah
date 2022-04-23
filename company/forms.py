from django import forms
from django.core import validators
from company.models import ContactUsModel

class ContactUsForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = ContactUsModel
        fields = ('name','email','phone_number','request')
        widgets = {
            'name': forms.TextInput(attrs={'class':'uk-input fYekan redC-text','placeholder':''},),
            'phone_number': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':'مانند: ۰۹۱۴۱۱۶۵۹۱۳'},),
            'request': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'4','placeholder':'هر گونه انتقاد پیشنهاد یا درخواستی از ما دارید با ما در میان بگذارید'},),
            'email': forms.EmailInput(attrs={'class':'uk-input fYekan','placeholder':'مانند: info@soolenavvah.com'},),

        }
