from django import forms
from django.core import validators
from ordering.models import OrderingModel


class OrderingForm(forms.ModelForm):

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = OrderingModel
        fields = ('phone_number','length','width','address','name','height','type_of_use',
                'number_of_floor','has_child_salon','has_half_floor','has_crane','crane_weight',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'class':'uk-input fYekan redC-text','placeholder':''},),
            'length': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'width': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'height': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'name': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'type_of_use': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'number_of_floor': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),
            'crane_weight': forms.TextInput(attrs={'class':'uk-input fYekan','placeholder':''},),

            'address': forms.Textarea(attrs={'class':'uk-textarea fYekan','rows':'3','placeholder':'محل نصب سالن'},),

        }
